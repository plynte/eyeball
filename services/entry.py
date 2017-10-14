#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,render_to_response

def hello(request):
    # return HttpResponse('ok')
    return render(request,'test.html')
def add2(request):
    return HttpResponse('add2')