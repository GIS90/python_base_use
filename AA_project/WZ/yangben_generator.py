# -*- coding: utf-8 -*-
"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import codecs

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/1/19"

fw = codecs.open('gps.txt', mode='w', encoding='utf8')
with open('data.txt') as fr:
    lines = fr.readlines()
    for line in lines:
        data = line.split('message: ')[-1]
        fw.write(data)

fw.close()






