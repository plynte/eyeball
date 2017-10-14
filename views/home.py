#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render,HttpResponse

def index(request):
    # return HttpResponse('index')
    return render(request,'index.html')
    # return render(request,'websock_test.html')