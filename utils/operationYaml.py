#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import yaml
from common.public_path import getFilePath
from utils.operationExcel import OperationExcel

class OperationYaml(object):
    def __init__(self,dirName,fileName):
        self.dirName = dirName
        self.fileName = fileName

    # 获取yaml文件数据，返回字典
    def getYaml_dict(self):
        try:
            f = open(file=getFilePath(dirName=self.dirName,fileName=self.fileName))
        except:
            OperationExcel().writeLogs()
        return yaml.safe_load(stream=f)
    # 获取yaml文件数据，返回列表
    def getYaml_list(self):
        try:
            f = open(file=getFilePath(dirName=self.dirName,fileName=self.fileName))
        except:
            OperationExcel().writeLogs()
        return list(yaml.safe_load_all(stream=f))

    # 写入指定数据到yaml文件
    def writeYaml(self,content):
        try:
            f = open(file=getFilePath(dirName="datas",fileName="data.yaml"),encoding="UTF-8",mode="w")
        except:
            OperationExcel().writeLogs()
        return yaml.dump(data=content,stream=f,allow_unicode=True)

    # 普通文本的读取
    def readText(self):
        try:
            f = open(file=getFilePath(dirName=self.dirName,fileName=self.fileName))
        except:
            OperationExcel().writeLogs()
        return f.read()

    # 普通文本写入
    def writeText(self,content):
        try:
            f = open(file=getFilePath(dirName=self.dirName,fileName=self.fileName),mode="w")
        except:
            OperationExcel().writeLogs()
        f.write(content)

    # 获取映射参数
    def get_mapping_ExcelToYaml(self,key):
        if key == "" or key == None:
            return None
        else:
            return self.getYaml_dict()[key]

if __name__ == '__main__':
    old_realName = OperationYaml(dirName="datas",fileName="data.yaml").getYaml_dict()
    print(old_realName)