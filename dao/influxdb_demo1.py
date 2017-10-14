#! /usr/bin/env python
# -*- coding:utf-8 -*-
from influxdb import InfluxDBClient
import time

def func1():
    cli = InfluxDBClient.from_dsn(dsn='influxdb://root:root@192.168.104.110:8087/lepus',**{"timeout":5})
    # cli = InfluxDBClient(host='192.168.104.110',port=8087,username='root',password='root',database='lepus')
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server03",
                "region": "cn-east"
            },
            "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime()),
            "fields": {
                "value": 0.64
            }
        },
        {
            "measurement": "cpu_load_avg",
            "tags": {
                "host": "server04",
                "region": "cn-east"
            },
            "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime()),
            "fields": {
                "value": 0.22
            }
        }
    ]

    json_body_2 = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime()),
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True,
                "Shor_value": 0.6
            }
        }
    ]
    json_body_3 = [
        {
            "measurement": "mysql_uptime",
            "tags": {
                "host": "192.168.200.135",
                "region": "devops"
            },
            "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime()),
            "fields": {
                "Float_value": 100000577.00,
            }
        }
    ]

    try:
        REVAL = cli.write_points(json_body_3)
        print REVAL
    except Exception as e:
        print str(e)

    # print cli.request(url='query',params='q=SHOW MEASUREMENTS').json()

    # cli.delete_series(database='lepus',measurement='cpu_load_short')
    # cli.delete_series(database='lepus',measurement='cpu_load_short',tags={"host": "server02"})
    # cli.drop_measurement(measurement='cpu_load_short')
    # res = cli.query('select * from cpu_load_short')
    # res = cli.query('select value,host,region from cpu_load_short')
    # print res
    # print res.items()
    # print list(res.get_points(measurement='cpu_load_short'))

    print cli.get_list_database()
    print cli.get_list_measurements()
    cli.close()
def func2():
    # 2011-11-10T23:00:00Z
    print time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
    # print time.localtime(time.time())

if __name__ == '__main__':
    func1()
    # func2()