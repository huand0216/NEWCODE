#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import os

def getFilePath(dirName,fileName):
    try:
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),dirName,fileName)
    except BaseException as e:
        return e
    return path

if __name__ == '__main__':
    print(getFilePath(dirName="datas",fileName="test.txt"))




