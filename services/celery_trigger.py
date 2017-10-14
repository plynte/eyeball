#! /usr/bin/env python
# -*- coding:utf-8 -*-
#trigger.py
import time,sys
from tasks import add,test_mes


# result = add.delay(4, 4) #不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
# print result.ready()
# print result.status
# print result.get('p')
# while not result.ready():
#     print result.get('p')
#     time.sleep(1)
# print 'task done: {0}'.format(result.get())


def pm(body):
    res = body.get('result')
    # print body.get('status')

    if body.get('status') == 'PROGRESS':
        # print res.get('p')
        sys.stdout.write('\r任务进度: {0}%'.format(res.get('p')))
        sys.stdout.flush()
    else:
        print '\r'
        # sys.stdout.flush()
        print 'res-->',res

r = test_mes.delay()
r.get(on_message=pm, propagate=False)