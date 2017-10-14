#!/usr/bin/env python
# -*- coding: utf8 -*-
import pika
import json
from settings import BROKER_HOST,BROKER_PORT

class Msg():
    def __init__(self):
        credentials = pika.PlainCredentials('guest', 'guest')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=BROKER_HOST, port=BROKER_PORT, credentials=credentials))
        self.channel = self.connection.channel()


    def sent(self,data,queue='deployitems'):
        '''发送data到队列，生产者'''
        # print str(type(data)).find('str')

        if str(type(data)).find('dict') != -1:
            self.channel.queue_declare(queue=queue , durable=True)  # durable=True 声明队列持久化
            self.channel.basic_publish(exchange='',
                                  routing_key=queue,
                                  body=json.dumps(data),
                                  properties=pika.BasicProperties(delivery_mode=2, )  # 使消息或任务也持久化存储
                                  )
            # self.connection.close()
            return True,"[RabbitMQ] Sent msg to %s:%s " %(queue,data)
        else:
            return False,'param error...'



if __name__ == '__main__':
    msg = Msg()
    data = {"domain_name": "app.ppmoney.com","commit_id": "854566325634497545622123336446621","deploy_type": "prod"}
    msg.sent(data)
    # msg.receive()