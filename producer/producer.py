from flask import Flask
import pika
import atexit

app = Flask(__name__)

# Setup of connection
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='hello')

# Connection must be closed when we are done
atexit.register(connection.close)

@app.route('/')
def send_message():
    channel.basic_publish(routing_key='hello',
                          body='Hey bud, someone visited me',
                          exchange='')
    return {'body': 'Thanks for visiting!'}, 200
