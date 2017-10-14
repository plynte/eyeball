#! /usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class CMDB(models.Model):
    '''models IP 域名'''
    domain = models.CharField(u'域名',max_length=64, unique=True)
    IP = models.CharField(u'域IP',max_length=64, unique=True)
    developer = models.CharField(u'开发者',max_length=32,)
    systemadmin = models.CharField(u'运维者',max_length=32,)
    class Meta:
        verbose_name_plural = "CMDB"


'''审批通过 1 不通过 0'''
class Approve(models.Model):
    # is_approve = models.CharField(u'审批',max_length=2,unique=True)
    is_approve = models.BooleanField(u'审批')
    class Meta:
        verbose_name_plural = "approve"

'''post 过来的 待发布 项'''
class DeployItems(models.Model):
    deploy_sn = models.CharField(u'序列号',max_length=64,unique=True)
    domain_name = models.CharField(u'域名', max_length=64)
    commit_id = models.CharField(u'版本号', max_length=64)
    deploy_type = models.CharField(u'发布类型', max_length=32)
    is_approve = models.ForeignKey(Approve, on_delete=models.CASCADE,null=True)
    class Meta:
        verbose_name_plural = "DeployItems"


'''已发布 项'''
class Deploy(models.Model):
    '''models IP 域名'''
    domain = models.CharField(u'域名',max_length=64)
    IP = models.CharField(u'域IP',max_length=64)
    deploy_type = models.CharField(u'发布类型',max_length=32)
    version = models.CharField(u'发布版本',max_length=128, unique=True)
    class Meta:
        verbose_name_plural = "Deploy"
'''发布日志'''
class Deploylog(models.Model):
    '''models IP 域名'''
    domain = models.CharField(u'域名',max_length=64)
    IP = models.CharField(u'发布IP',max_length=64)
    deploy_type = models.CharField(u'发布类型',max_length=32)
    version = models.CharField(u'发布版本',max_length=128)
    operator = models.CharField(u'操作人',max_length=32)
    action_time = models.DateTimeField(u"执行时间", default=timezone.now)
    class Meta:
        verbose_name_plural = "DeployLog"



# Create your models here.

# class Reporter(models.Model):
#     full_name = models.CharField(max_length=70)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.full_name
#
# class Article(models.Model):
#     pub_date = models.DateField()
#     headline = models.CharField(max_length=200)
#     content = models.TextField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.headline

# if __name__ == '__main__':
#     c = CMDB(domain='app1.ppmoney.com',IP='10.10.10.112',developer='张三，李四',systemadmin='王五，刘六')
#     c.save()