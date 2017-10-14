#! /usr/bin/env python
# -*- coding:utf-8 -*-
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")# project_name 项目名称
django.setup()

import pika
import json
from settings import BROKER_HOST,BROKER_PORT
from model.models import DeployItems


class Consumer():
    def __init__(self):
        credentials = pika.PlainCredentials('guest', 'guest')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=BROKER_HOST, port=BROKER_PORT, credentials=credentials))
        self.channel = self.connection.channel()
    def receive(self, queue='deployitems'):
        self.data = ''
        self.channel.queue_declare(queue=queue, durable=True)
        def callback(ch, method, properties, body):
            self.save(body)
        self.channel.basic_consume(callback, queue=queue, no_ack=True)
        self.channel.start_consuming()


    def save(self, body):
        data = json.loads(body)
        print type(body),body
        print type(data),data
        try:
            D = DeployItems.objects.create(**data)
            # deploy_sn = data['deploy_sn'], domain_name = data['domain_name'], commit_id = data['commit_id'], deploy_type = data['deploy_type']
            # D = DeployItems(deploy_sn=data['deploy_sn'],domain_name=data['domain_name'],commit_id=data['commit_id'],deploy_type=data['deploy_type'])
            D.save()
        except Exception as e:
            print str(e)


if __name__ == '__main__':
    c = Consumer()
    c.receive()