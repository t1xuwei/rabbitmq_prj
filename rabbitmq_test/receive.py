# coding=utf-8
import pika
'''
接收rabbitmq发送的信息
'''

connection = pika.BlockingConnection(pika.ConnectionParameters(  
        host='localhost'))
channel = connection.channel()  
  
#channel.queue_declare(queue='route_k')  
  
print ' [*] Waiting for messages. To exit press CTRL+C'  
  
def callback(ch, method, properties, body):  
    print " [x] Received: %r!!" % (body,)  
  
channel.basic_consume(callback,  
                      queue='hello',
                      no_ack=True)  
  
channel.start_consuming()  
