#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render,HttpResponse

def lepus_chart(request):
    return render(request,'lepus_chart.html')
def lepus_table(request):
    return render(request,'lepus_table.html')