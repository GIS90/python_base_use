# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
冒泡排序
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/1"


def maopao(l):

    count = len(l)
    for i in range(0, count):
        for j in range(i + 1, count):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l








