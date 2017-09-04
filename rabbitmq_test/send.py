import pika  
  
connection = pika.BlockingConnection(pika.ConnectionParameters(  
        host='localhost'))  
channel = connection.channel()  
  
channel.queue_declare(queue='hello')  
  
channel.basic_publish(exchange='',  
                      routing_key='route_k',  
                      body='Hello  wei!')  
print " [x] Sent 'Hello World!'"  
connection.close()  
