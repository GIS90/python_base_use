# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/29'
"""
import codecs
from JsFormat import *
from Log import *
from AnlyConfigFile import *


def WtToFile(fp, num, data):
    assert isinstance(fp, basestring)
    assert isinstance(data, list)
    assert isinstance(num, int)
    if not data:
        return 0
    n = 0
    if os.path.exists(fp):
        os.unlink(fp)
    fw = codecs.open(fp, mode='w', encoding='utf-8')
    try:
        contPre = GetJsPreFix()
        fw.write(contPre)
        fw.write('=[')
        fw.write('\n')
        for line in data:
            fw.write('\t')
            v1 = line[0]
            v2 = line[1]
            line = '{"name":"%s","value":%s}' % (v1, v2)
            fw.write(line)
            fw.write(',') if n < num-1 else 0
            n += 1
            fw.write('\n')
        fw.write(']')
        return 1
    except Exception as we:
        Log('ERROR', 'WtToFile Occur Exception : %s' % we.message)
        return 0
    finally:
        fw.close()



