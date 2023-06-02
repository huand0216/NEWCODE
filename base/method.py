#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import requests
import pytest

'''
重新封装requests方法
'''
class My_request(object):
    # 通用请求方法
    def my_request(self,url,method,**kwargs):
        try:
            return requests.request(url=url,method=method,**kwargs)
        except BaseException as e:
            return e.args

    # GET请求方法
    def GET(self,url,**kwargs):
        try:
            return requests.get(url=url,**kwargs)
        except BaseException as e:
            return e.args

    # POST请求方法
    def POST(self,url,**kwargs):
        try:
            return requests.post(url=url,**kwargs)
        except BaseException as e:
            return e.args

if __name__ == '__main__':
    token = "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIxNDA1MTQzIiwidXNlcl9uYW1lIjoiMTg1NjU4MDY0NzciLCJyZWFsX25hbWUiOiLog6HlronkuJwiLCJhdmF0YXIiOiIiLCJhdXRob3JpdGllcyI6WyIxNTE4ODY1OTk4MDUxOTM0MjA5Il0sImNsaWVudF9pZCI6Im1lY2hjIiwicm9sZV9uYW1lIjoiYWRtaW4iLCJsaWNlbnNlIjoicG93ZXJlZCBieSBibGFkZXgiLCJwb3N0X2lkIjoiIiwidXNlcl9pZCI6IjE1Mzk4MDc3MTEyODAxMjgwMDIiLCJyb2xlX2lkIjoiMTUxODg2NTk5ODA1MTkzNDIwOSIsInNjb3BlIjpbImFsbCJdLCJuaWNrX25hbWUiOiLog6HlronkuJwiLCJvYXV0aF9pZCI6IiIsImRldGFpbCI6eyJ2ZXJpZnlQYXNzV29yZCI6dHJ1ZSwiaW5kdXN0cnkiOjMsInRlbmFudE5hbWUiOiLmmbrmhaflhbvogIHpmaIifSwiZXhwIjoxNjU3MDg5Njk2LCJkZXB0X2lkIjoiMTUxODg4MDAyMjY2Nzg1MzgyNiIsImp0aSI6IjM3MzYzYjY1LWIxNGUtNGU2MS1iMjA0LTQ5MDMzYjNjODhjYyIsImFjY291bnQiOiIxODU2NTgwNjQ3NyJ9.uai4rrhxVbsglhzsFfxHBSgSGaPby1OVEzUSuhP_ZZk"
    obj = My_request()
    url = "http://new.baisuiyun.com/api/mechc/mechc-organ/organlkelderlyinfo/list"
    headers = {"Blade-Auth":token}
    params = {"current": 1, "size": 10}
    res = obj.GET(url=url,params=params,headers = headers)
    print(res.json())