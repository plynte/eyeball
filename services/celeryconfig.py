#! /usr/bin/env python
# -*- coding:utf-8 -*-
broker_url = 'pyamqp://guest@192.168.200.135//'
result_backend = 'redis://192.168.200.128:6379'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True
result_expires = 3600
# task_routes = {
#     'tasks.add': 'low-priority',
# }

'''
only 10 tasks of this type can be processed in a minute (10/m)
'''
task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}