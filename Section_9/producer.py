import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

queue_name = 'first_rabbitmq'

channel.queue_declare(queue=queue_name)

with open('messages.txt', 'r') as f_msgs:
	lines = f_msgs.readlines()

	for line in lines:
		line = line.strip()

		channel.basic_publish(exchange='',
							routing_key=queue_name,
							body=line)

		print("Sent Message :", line)
		
		print("Now sleeping for 2 seconds")
		time.sleep(2)

connection.close()