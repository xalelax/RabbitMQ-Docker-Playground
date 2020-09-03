from flask import Flask
app = Flask(__name__)


@app.route('/')
def send_message():
    return {'body': 'Thanks for visiting!'}, 200
