import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

queue_name = 'first_rabbitmq'

channel.queue_declare(queue=queue_name)

def consume_msg(ch, method, properties, body):
    print("Consumed Message {}".format(body))

channel.basic_consume(queue=queue_name,
					on_message_callback=consume_msg,
					auto_ack=True)

print('Now consuming messages from producer')

channel.start_consuming()
