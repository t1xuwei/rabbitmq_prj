# coding=utf-8
import pika

credentials = pika.PlainCredentials('xuw', 'xuw@123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='115.159.149.177', credentials=credentials))
channel = connection.channel()

queue = channel.queue_declare(queue='hello', arguments={'x-max-length': 10})

for index in range(0, 100):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=('Hello  wei!,i am %d' % index))

def del_queue_by_name(channel, queue_name):
    channel.queue_delete(queue_name)
# del_queue_by_name(channel,"hello")

print " [x] Sent 'Hello World!'"
connection.close()
