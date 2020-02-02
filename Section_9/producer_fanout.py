import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

queue_name = 'my_rabbitmq_fanout'
exchange_name = 'myfanout_exchange'

channel = connection.channel()

channel.exchange_declare(exchange=exchange_name,
						exchange_type='fanout')

# channel.queue_declare(queue=queue_name)

with open('messages.txt', 'r') as f_msgs:

	lines = f_msgs.readlines()
	for line in lines:
		
		line = line.strip()
		
		channel.basic_publish(exchange=exchange_name,
							routing_key='',
							body=line)
		print("Sent Message :", line)
		print("Now sleeping for 2 seconds")
		time.sleep(2)

connection.close()