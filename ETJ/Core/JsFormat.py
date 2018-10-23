# -*- coding: utf-8 -*-

import re
from AnlyConfigFile import *
from Log import *

try:
    js = Config_Js
    with open(js) as fr:
        content = fr.read()
    fr.close()
except Exception as e:
    Log('ERROR', 'JsFormat Init Occur Exception : %s' % e.message)


def GetJsPreFix():
    preFix = content.split('=')[0]
    return preFix


def GetJsSufFix():
    sufFix = content.split('=')[1]
    return sufFix


def GetJsType():
    """
    对示例的Js文件进行类型判断
    :return: 如果是=[，返回1
             如果是={，返回2
    """
    reg = ['.*=\[.*', '.*=\{.*']
    for reV in reg:
        pattern = re.compile(reV, re.M)
        results = re.search(pattern, content)
        if results and reV == '.*=\[.*':
            return 1
        elif results and reV == '.*=\{.*':
            return 2
        else:
            pass
