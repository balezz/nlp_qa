#!/usr/bin/python
import sox.file_info
from flask import Flask, render_template, request
from pathlib import Path
from engine import vosk_decode, compare_answer

# create and initialize a new Flask app
app = Flask(__name__)

# configuration
app.config.from_object(__name__)
app.config['ALLOWED_EXTENSIONS'] = ['wav']
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
app.config['WAV_FOLDER'] = Path('waves')


@app.route('/')
def index():
    quest = {'quest': 'Дайте определение войны?'}
    return render_template('index.html', quest=quest)


@app.route('/', methods=['POST'])
def api_message():
    if request.method == 'POST':
        filename = 'file.wav'
        wav_path = str(app.config['WAV_FOLDER'] / filename)
        print(request.files)
        data = request.files['voice'].read()
        with open(wav_path, 'wb') as f:
            f.write(data)
        wav_info = sox.file_info.info(wav_path)
        print('Duration: ' + str(round(wav_info['duration'], 2)) + ' sec')
        answer = vosk_decode(wav_path)
        print(answer)
        result = compare_answer(answer)
        response = f'Оценка - {result} / 10'
        print(response)
        return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
