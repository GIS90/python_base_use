# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
插入排序
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/1"


def charu(l):
    count = len(l)
    for i in range(1, count):
        key = l[i]
        j = i - 1
        while j > 0:
            if l[j + 1] > key:
                l[j + 1], l[j] = l[j], key
            j -= 1

    return l
