from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f'Hello, World! j2 {datetime.datetime.now()}'

@app.route('/about')
def about():
    return 'About'