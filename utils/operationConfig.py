#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import configparser
from common.public_path import getFilePath


def get_configparser(environment):
    config = configparser.ConfigParser()
    config.read(filenames=getFilePath(dirName="config",fileName="configparser.ini"))
    return dict(config.items(environment))


if __name__ == '__main__':
    print(get_configparser(environment="test"))


