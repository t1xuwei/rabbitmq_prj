# coding=utf-8
import pika

credentials = pika.PlainCredentials('xuw', 'xuw@123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='115.159.149.177', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello', arguments={'max-length': 10})

for index in range(0, 100):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=('Hello  wei!,i am %d' % index))

print " [x] Sent 'Hello World!'"
connection.close()
