# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
希尔排序
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/1"


def xier(l):
    count = len(l)
    step = count / 2
    while step > 0:
        for i in range(step, count):
            while i >= step and l[i - step] > l[i]:
                l[i], l[i - step] = l[i - step], l[i]
                i -= step
        step /= 2
    return l
