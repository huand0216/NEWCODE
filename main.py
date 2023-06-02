#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong
import os

import pytest
from common.public_path import getFilePath
import allure

if __name__ == '__main__':

    pytest.main(["-v", "-s","./tests/","--alluredir=./report/result","--clean-alluredir"])

    os.system("allure generate ./report/result -o ./report/result/html --clean")

    os.system("allure serve ./report/result")