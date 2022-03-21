import sox
import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
from deeppavlov.core.common.file import read_json
from deeppavlov import build_model, configs
from scipy import spatial
import data


def vosk_decode(wave_path):
    SetLogLevel(0)

    wf = wave.open(wave_path, "rb")

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        exit(1)

    model = Model("vosk-model-small")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # print(rec.Result())
            pass
        else:
            pass
            # print(rec.PartialResult())

    res = rec.FinalResult()
    return json.loads(res)['text']


def compare_answer(my_answer):
    right_answer = data.answer
    texts = [my_answer, right_answer]

    bert_config = read_json(configs.embedder.bert_embedder)
    bert_config['metadata']['variables']['BERT_PATH'] = 'rubert'
    rubert_model = build_model(bert_config)

    # Эмбеддинги имеют размер: (количества токенов в ответе, 768)
    # 768 - длина вектора внутреннего состояния модели RuBERT
    # Вычисляем эмбеддинги для каждого ответа
    tokens, token_embs, subtokens, subtoken_embs, sent_max_embs, sent_mean_embs, bert_pooler_outputs = rubert_model(
        texts)

    sentense_embed = []
    # Усредняем по токенам - словам в предложении
    for te in token_embs:
        sentense_embed.append(te.mean(axis=0))

    cs = spatial.distance.cosine(sentense_embed[0], sentense_embed[1])
    result = int(round(cs * 10))
    return result


if __name__ == '__main__':
    wav_path = 'waves/war_1.wav'
    wav_info = sox.file_info.info(wav_path)
    info = {
        'Длительность аудио': str(round(wav_info['duration'], 2)) + ' с',
        'Число каналов': wav_info['channels'],
        'Частота дискретизации': str(int(wav_info['sample_rate'])) + ' Гц'
    }
    print(info)

    my_answer = vosk_decode(wav_path)
    result = compare_answer(my_answer)

    print(f'Оценка - {result} / 10')
