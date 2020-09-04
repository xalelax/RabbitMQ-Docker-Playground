from flask import Flask
import pika

app = Flask(__name__)

@app.route('/')
def send_message():
    channel.basic_publish(routing_key='hello',
                          body='Hey bud, someone visited me',
                          exchange='')
    return {'body': 'Thanks for visiting!'}, 200

if __name__ == 'producer':
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')