#!/usr/bin/python

from flask import Flask, render_template, request
from pathlib import Path
from engine import vosk_decode, score_answer
from data import DATA

i = 0

# create and initialize a new Flask app
app = Flask(__name__)

# configuration
app.config.from_object(__name__)
app.config['ALLOWED_EXTENSIONS'] = ['wav']
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
app.config['WAV_FOLDER'] = Path('waves')


@app.route('/', methods=['GET'])
def index():
    quest = {'quest': f'Дайте определение: {getDATA()}'}
    #return jsonify('index.html', quest=quest)
    return render_template('index.html', quest=quest)


@app.route('/', methods=['POST'])
def api_message():
    if request.method == 'POST':
        filename = 'file_{}.wav'.format(i-1) 
        wav_path = str(app.config['WAV_FOLDER'] / filename)
        print(request)
        data = request.files['voice'].read()
        with open(wav_path, 'wb') as f:
            f.write(data)
        my_answer = vosk_decode(wav_path)
        right_answer = DATA[0][1]
        result = score_answer(my_answer, right_answer)
        print(f'You: {my_answer}')
        print(f'Right: {right_answer}')
        response = f'Score - {int(round(10*result))} / 10'
        print(response)
        return response


def getDATA():
    global i
    data_value = DATA[i][0]
    i += 1
    return data_value


if __name__ == "__main__":
    app.run()
