import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

queue_name = 'my_direct_age_queue'
exchange_name = 'my_direct_exchange'

channel.exchange_declare(exchange=exchange_name,
					exchange_type='direct')

channel.queue_declare(queue=queue_name, exclusive=True)

channel.queue_bind(exchange=exchange_name,
				queue=queue_name,
				routing_key='Age')

def consume_msg(ch, method, properties, body):
    print("Age of the user is {}".format(body))

channel.basic_consume(queue=queue_name,
					on_message_callback=consume_msg,
					auto_ack=True)

print('Now consuming messages from producer by Age Consumer')

channel.start_consuming()