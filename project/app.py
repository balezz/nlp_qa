import sqlite3
from flask import Flask, render_template, request, json

# configuration

# create and initialize a new Flask app
app = Flask(__name__)

# load the config
app.config.from_object(__name__)


@app.route('/')
def index():
    quest = {'quest': 'Дайте определение войны.'}
    return render_template('index.html', quest=quest)


@app.route('/wave', methods=['POST'])
def wave():
    print('Get wav file')
    return json.dumps({'status': 'OK'})


if __name__ == "__main__":
    app.run()
