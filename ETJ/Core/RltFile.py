# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/29'
"""

from AnlyConfigFile import *


def GetRlt():
    """
    获取生成目标文件的名称以及路径
    :return: 名称，路径
    """
    RltName = RF_NAME + RF_TYPE
    RltPath = RF_PATH
    return RltName, RltPath
