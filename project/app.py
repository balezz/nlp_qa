import sqlite3
from flask import Flask, render_template, request

# configuration

# create and initialize a new Flask app
app = Flask(__name__)

# load the config
app.config.from_object(__name__)


@app.route('/')
def index():
    quest = {'quest': 'Дайте определение войны?'}
    return render_template('index.html', quest=quest)
    
@app.route('/', methods = ['POST'])
def api_message():
      f = open('./file.wav', 'wb')
      f.write(request.data)
      f.close()
      return "Voice written!"

if __name__ == "__main__":
    app.run()
