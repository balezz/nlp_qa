import sqlite3
from flask import Flask, render_template

# configuration

# create and initialize a new Flask app
app = Flask(__name__)

# load the config
app.config.from_object(__name__)


@app.route('/')
def index():
    quest = {'quest': 'Дайте определение войны.'}
    return render_template('index.html', quest=quest)


if __name__ == "__main__":
    app.run()
