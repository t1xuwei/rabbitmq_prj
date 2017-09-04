# coding=utf-8
import pika
credentials = pika.PlainCredentials('xuw', '')
connection = pika.BlockingConnection(pika.ConnectionParameters(  
        host='115.159.149.177',credentials=credentials))
channel = connection.channel()  
  
channel.queue_declare(queue='hello')  
  
channel.basic_publish(exchange='',  
                      routing_key='route_k',  
                      body='Hello  wei!')  
print " [x] Sent 'Hello World!'"  
connection.close()  
