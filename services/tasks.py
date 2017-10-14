#! /usr/bin/env python
# -*- coding:utf-8 -*-
from celery import Celery
import time
'''
Celery 的第一个参数是当前模块的名称，这个参数是必须的，这样的话名称可以自动生成
第二个参数是中间人关键字参数，指定你所使用的消息中间人的 URL，此处使用了 RabbitMQ，也是默认的选项。
'''
# app = Celery('tasks',deploy='redis://192.168.200.128:6379',broker='pyamqp://guest@192.168.200.135//') #deploy='amqp'
app = Celery('tasks') #deploy='amqp'
app.config_from_object('celeryconfig')

@app.task #普通函数装饰为 celery task
def add(x,y):
    # print 'ppmoney'
    return x + y


@app.task(bind=True)
def test_mes(self):
    for i in xrange(1, 11):
        time.sleep(0.1)
        self.update_state(state="PROGRESS", meta={'p': i*10})
    return 'finish'