#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.http import StreamingHttpResponse,HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import settings
import os

@csrf_exempt
@require_http_methods(["GET"])
def downloadFile(request):
    md5 = request.GET.get("md5")
    fileName = '%s.war'%md5
    file_name = os.path.join(settings.UPLOADFILES_DIRS, fileName)
    if os.path.exists(file_name):

        response = StreamingHttpResponse(file_iterator(file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(fileName)
        return response
    else:
        return HttpResponse('{"success": -1 , "message":"文件不存在"}')

def file_iterator(file_name, chunk_size=512):
    with open(file_name) as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break