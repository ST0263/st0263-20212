# producer.py
# This script will publish MQ message to my_exchange MQ exchange

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('52.91.253.91', 5672, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()

channel.basic_publish(exchange='my_exchange', routing_key='test', body='Test!')
print("Runnning Producer Application...")
print(" [x] Sent 'Hello World...!'")

connection.close()  