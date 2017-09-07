# coding=utf-8
import pika
import time

'''
basic qos test
'''

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# channel.queue_declare(queue='route_k')

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received: %r!!" % (body,)
    time.sleep(1)
    # 对msg进行确认
    # channel.basic_ack(method.delivery_tag)


# 设定消费者每次最多消费一个信息
channel.basic_qos(prefetch_count=1)

# no_ack为false时，每次启动接收脚本都会收到队列里面的信息
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
