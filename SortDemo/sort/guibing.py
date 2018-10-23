# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
归并排序
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/1"


def guibing(l):
    count = len(l)
    if count <= 1:
        return l
    step = count / 2
    left = guibing(l[:step])
    right = guibing(l[step:])

    def merge(left, right):
        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    return merge(left, right)
