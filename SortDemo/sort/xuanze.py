# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
选择排序
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/1"


def xuanze(l):
    count = len(l)
    for i in range(0, count):
        minloc = i
        for j in range(i + 1, count):
            if l[minloc] > l[j]:
                minloc = j
        l[minloc], l[i] = l[i], l[minloc]

    return l
