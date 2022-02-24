#!/usr/bin/python
import os
import sqlite3
import sox.file_info
from flask import Flask, render_template, request
from pathlib import Path

# create and initialize a new Flask app
from engine import recognize

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
    filename = 'file.wav'
    wav_path = str(app.config['WAV_FOLDER'] / filename)
    with open(wav_path, 'wb') as f:
        f.write(request.data)
    # wav_info = sox.file_info.info('/home/user/ds/PycharmProjects/nlp_qa/project/waves/file.wav')
    # print('Duration: ' + str(round(wav_info['duration'], 2)) + ' sec')
    temp = str(app.config['WAV_FOLDER'] / Path(wav_path).stem)
    os.makedirs(temp, exist_ok=True)
    # transcriptions = recognize(temp, wav_path)
    return "Voice written!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
