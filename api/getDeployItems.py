#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from services.msg import Msg
from dwebsocket.decorators import accept_websocket,require_websocket

import pika,json
from settings import BROKER_HOST,BROKER_PORT
from model.models import DeployItems

'''
POST 部署项的信息API 提供外部系统使用
'''
@csrf_exempt
def getDeployItems(request):
    if request.method == 'POST':
        # cmd = json.loads(request.body)['cmd']
        post_data = eval(request.body)['data']
        print type(post_data)
        domainName = post_data['domain_name']
        commitId = post_data['commit_id']
        deployType = post_data['deploy_type']
        deploy_sn = post_data['deploy_sn']
        # result = commands.getstatusoutput(cmd) # 在win上会有乱码
        # out = result[1].replace("\n", "<br/>").replace('"', '\\"')

        '''把post data 发送到消息队列deployitems中'''
        data = {"domain_name":domainName,"commit_id":commitId,"deploy_type":deployType,"deploy_sn":deploy_sn}
        tag,ret = Msg().sent(data)

        # '''直接把post的数据存入数据库'''
        # tag = True
        # ret = 'ok'
        # try:
        #     D = DeployItems.objects.create(**post_data)
        #     D.save()
        # except Exception as e:
        #     tag = False
        #     ret = 'Error'
        #     print str(e)

        if tag :
            res = '{"success":true,"result":0,"message":"%s"}' % (ret)
            return HttpResponse(res)
        else:
            res = '{"success":false,"result":1,"message":"%s"}'% ret
            return HttpResponse(res)
    else:
        res = '{"success":false,"result":1,"data":"403 Forbidden"}'
        return HttpResponse(res)

@csrf_exempt
@accept_websocket
# @require_websocket
def deployitems(request):
    # if request.is_websocket():
    #     request.websocket.send('cao')  # 发送消息到客户端
    # else:
    #     return HttpResponse('he')
    if not request.is_websocket():  # 判断是不是websocket连接
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'websock_test.html')
    else:
        def callback(ch, method, properties ,body):
            print '收到消息：-->',type(body),json.dumps(json.loads(body))
            request.websocket.send(json.dumps(json.loads(body)))
        C.receive(callback=callback)

class Consumer():
    def __init__(self):
        credentials = pika.PlainCredentials('guest', 'guest')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=BROKER_HOST, port=BROKER_PORT, credentials=credentials))
        self.channel = self.connection.channel()
        # Consumer().receive()
    def receive(self, callback,queue='deployitems'):
        self.channel.queue_declare(queue=queue, durable=True)
        self.channel.basic_consume(callback, queue=queue, no_ack=True)
        self.channel.start_consuming()

C = Consumer()