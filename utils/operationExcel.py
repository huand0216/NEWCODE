#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

from common.public_path import getFilePath
import xlrd
import xlwt
import traceback

class OperationExcel(object):
    CASE_ID = "用例ID"
    REMARKS = "用例描述"
    URL = "地址"
    METHOD = "请求方法"
    PARAMETER = "参数"
    EXPECT = "预期结果"

    def __init__(self,dirName = "datas",fileName = None,sheetName = None):
        '''
        @param dirName: Excel文件上级目录名称
        @param fileName: Excel文件名称
        @param sheetName: sheet名称
        '''
        self.dirName = dirName
        self.fileName = fileName
        self.sheetName = sheetName

    # 将抛出日志写入日志文件的方法
    def writeLogs(self):
        with open(file=getFilePath(dirName="log",fileName="log.log"),mode="a") as f:
            traceback.print_exc(file=f)

    @property
    def getSheet(self):
        # book = xlrd.open_workbook(filename=getFilePath(dirName=self.dirName,fileName=self.fileName))
        try:
            with xlrd.open_workbook(filename=getFilePath(dirName=self.dirName,fileName=self.fileName)) as book:
                sheet = book.sheet_by_name(self.sheetName)
        except:
            self.writeLogs()
        return sheet

    # 有效行数
    def valid_raws(self):
        return self.getSheet.nrows

    # 有效列数
    def valid_cols(self):
        return self.getSheet.ncols

    # 获取Excel内数据，返回列表，列表内放字典
    def getExcelData(self):
        result = []
        try:
            key = self.getSheet.row_values(rowx=0)
            for idx in range(1,self.valid_raws()):
                value = self.getSheet.row_values(rowx=idx)
                data = dict(zip(key,value))
                result.append(data)
        except:
            self.writeLogs()
        return result

if __name__ == '__main__':
    o = OperationExcel(fileName="datas.xls",sheetName="datas")
    print(o.getExcelData())

