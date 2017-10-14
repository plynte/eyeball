# -*- coding:utf-8 -*-

"""celery_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from api.CommandRetHandler import CommandRet
from api.getDeployItems import getDeployItems,deployitems
from api.downloadFiles import downloadFile
urlpatterns = [
    url(r'^command', CommandRet, name='CommandRet'),
    url(r'^getdeployitems', getDeployItems, name='getDeployItems'),# 用于外部系统推送 发布信息过来
    url(r'^deployitems', deployitems, name='deployitems'),
    url(r'^download.do', downloadFile, name='downloadfiles'),
]
