import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

exchange_name = 'my_direct_exchange'

channel = connection.channel()

channel.exchange_declare(exchange=exchange_name,
						exchange_type='direct')

# channel.queue_declare(queue=queue_name)

with open('direct_messages.txt', 'r') as f_msgs:

	lines = f_msgs.readlines()
	for line in lines:
		
		line = line.strip()
		key, value = line.split(',')

		channel.basic_publish(exchange=exchange_name,
							routing_key=key,
							body=value)
		print("Sent Message :", line)
		print("Now sleeping for 2 seconds")
		time.sleep(2)

connection.close()