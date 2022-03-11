import sox
import wave
from vosk import Model, KaldiRecognizer, SetLogLevel


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
            print(rec.Result())
        else:
            print(rec.PartialResult())

    print(rec.FinalResult())


if __name__ == '__main__':
    wav_path = 'waves/war_1.wav'
    wav_info = sox.file_info.info(wav_path)
    info = {}
    info['Длительность аудио'] = str(round(wav_info['duration'], 2)) + ' с'
    info['Число каналов'] = wav_info['channels']
    info['Частота дискретизации'] = str(int(wav_info['sample_rate'])) + ' Гц'
    print(info)

    vosk_decode(wav_path)
