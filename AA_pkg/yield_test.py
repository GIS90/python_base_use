# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: yield_test.py
@time: 2016/8/30 13:55
@describe: 
@remark: 
------------------------------------------------
"""


def fab(MAX):
    n, a, b = 0, 0, 1
    while n < MAX:
        yield b
        a, b = b, a + b
        n += 1

MAX = 10
for i in fab(MAX):
    print i

