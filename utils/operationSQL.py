#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import pymysql
from utils.operationConfig import get_configparser

'''
链接数据库工具类
'''
class OperationSQL(object):

    data = get_configparser(environment="test")
    IP = data["IP"]
    PORT = data["port"]
    USER = data["user"]
    PASSWORD = data["password"]

    def connect(self,db):
        conn = pymysql.connect(
            host=self.IP,
            port=self.PORT,
            user=self.USER,
            password=self.PASSWORD,
            db=db
        )
        return conn

    def get_selectSql_dict(self,SQL,db):
        conn = self.connect(db=db)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(SQL)
        return cursor.fetchall()

    def get_selectSql_tuple(self,SQL,db):
        conn = self.connect(db=db)
        cursor = conn.cursor()
        cursor.execute(SQL=SQL)
        return cursor.fetchall()

    def updateSql(self,SQL,db):
        conn = self.connect(db=db)
        cursor = conn.cursor()
        cursor.execute(SQL=SQL)



