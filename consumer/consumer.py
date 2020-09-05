import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f"Received message: '{body}'")

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()