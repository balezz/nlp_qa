import asyncio

import numpy as np
import websockets
import wave
from data import DATA
from deeppavlov.core.common.file import read_json
from deeppavlov import build_model, configs

bert_config = read_json(configs.embedder.bert_embedder)
bert_config['metadata']['variables']['BERT_PATH'] = 'rubert'
rubert_model = build_model(bert_config)
VOSK_URI = 'ws://alphacep:2700'

async def kaldi_server_predict(uri, wav_path):
    result = []

    async with websockets.connect(uri) as websocket:
        wf = wave.open(wav_path, "rb")
        await websocket.send('{ "config" : { "sample_rate" : %d } }' % (wf.getframerate()))
        buffer_size = int(wf.getframerate() * 0.2) # 0.2 seconds of audio
        while True:
            data = wf.readframes(buffer_size)

            if len(data) == 0:
                break

            await websocket.send(data)
            result.append(await websocket.recv())

        await websocket.send('{"eof" : 1}')
        result.append(await websocket.recv())
    return result


def vosk_decode(wav_path, uri=VOSK_URI):
    print(f'start asr on {uri}')
    kaldi_result = asyncio.run(kaldi_server_predict(uri, wav_path))
    d = eval(kaldi_result[-1])
    return d['text']


def cosine_similarity(x, y):
    return x@y.T / (np.linalg.norm(x) * np.linalg.norm(y))


def score_answer(my_answer, right_answer):
    texts = [my_answer, right_answer]
    tokens, token_embs, _, _, _, sent_mean_embs, _ = rubert_model(texts)
    return cosine_similarity(*sent_mean_embs)


if __name__ == '__main__':
    wav_path = 'waves/war_1.wav'
    my_answer = vosk_decode(wav_path)
    right_answer = DATA[0][1]
    result = score_answer(my_answer, right_answer)

    print(f'Оценка - {result*10} / 10')
