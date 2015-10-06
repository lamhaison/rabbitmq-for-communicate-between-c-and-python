#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
#channel.queue_declare(queue='alanqueue')
channel.basic_publish(exchange='',
                      routing_key='alanqueue',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()

