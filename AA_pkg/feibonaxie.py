# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/23"


def fab(n):
    a, b, i = 0, 1, 0
    while i < n:
        a, b = b, a + b
        yield b
        i += 1


def charu(l):
    count = len(l)

    for i in range(0, count):
        key = l[i]
        j = i - 1
        while j >= 0:
            if l[j] > key:
                l[j + 1] = l[j]
                l[j] = key
            j -= 1

    print(l)


charu([123, 324, 23, 23, 234, 234, 234, 7])
