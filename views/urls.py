#-*- coding:utf-8 -*-
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
from lepus import lepus_chart,lepus_table
urlpatterns = [
    url(r'^command', CommandRet, name='CommandRet'),#

    url(r'^getdeployitems', getDeployItems, name='getDeployItems'),#接收发布项目信息接口，保存到DeployItems表
    url(r'^deployitems', deployitems, name='deployitems'),#websocket test 接口 用于前端展示实时接收后台推送的数据
    url(r'^download.do', downloadFile, name='downloadfiles'),#agentd 端 下载 代码包 接口
    url(r'^lepus_chart', lepus_chart, name='lepus_chart'),# 数据库监控
    url(r'^lepus_table', lepus_table, name='lepus_table'),# 数据库监控
]
