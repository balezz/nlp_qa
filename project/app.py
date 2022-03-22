#!/usr/bin/python
import sox.file_info
from flask import Flask, render_template, request
from pathlib import Path
from engine import vosk_decode, compare_answer
from data import DATA

# create and initialize a new Flask app
app = Flask(__name__)

# configuration
app.config.from_object(__name__)
app.config['ALLOWED_EXTENSIONS'] = ['wav']
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
app.config['WAV_FOLDER'] = Path('waves')


@app.route('/')
def index():
    quest = {'quest': f'Дайте определение: {DATA[0][0]}'}
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
        my_answer = vosk_decode(wav_path)
        right_answer = DATA[0][1]
        result = compare_answer(my_answer, right_answer)
        print(f'You: {my_answer}')
        print(f'Right: {right_answer}')
        response = f'Score - {result} / 10'
        print(response)
        return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
