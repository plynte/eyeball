#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,commands,subprocess

@csrf_exempt
def CommandRet(request):
    if request.method == 'POST':
        #django 获取post的json格式数据在 body 里面 和 tornado 一样。不能通过 request.POST.get()
        post_data = json.loads(request.body)['data']
        cmd = post_data['cmd']
        # cmd = eval(request.body)['data']['cmd']
        result = commands.getstatusoutput(cmd) # 在win上会有乱码
        out = result[1].replace("\n", "<br/>").replace('"', '\\"')
        print out
        res = '{"success":true,"result":0,"data":"%s"}' % (out)
        return HttpResponse(res)
    else:
        res = '{"success":true,"result":0,"data":"403 Forbidden"}'
        return HttpResponse(res)
