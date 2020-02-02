import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

queue_name = 'my_rabbitmq_fanout_2'
exchange_name = 'myfanout_exchange'

channel.exchange_declare(exchange=exchange_name,
					exchange_type='fanout')

channel.queue_declare(queue=queue_name, exclusive=True)

channel.queue_bind(exchange=exchange_name,
				queue=queue_name)

def consume_msg(ch, method, properties, body):
    print("Consumed Message {}".format(body))

channel.basic_consume(queue=queue_name,
					on_message_callback=consume_msg,
					auto_ack=True)

print('Now consuming messages from producer by Second Consumer')

channel.start_consuming()