#! /usr/bin/env python
# -*- coding:utf-8 -*-
from influxdb import DataFrameClient

def fun():
    cli = DataFrameClient(host='192.168.104.110',port=8087,username='root',password='root',database='lepus',timeout=5)
    print cli.query('select * from cpu_load_avg',dropna=True)

if __name__ == '__main__':
    fun()