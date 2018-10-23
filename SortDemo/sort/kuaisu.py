# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
快速排序
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/1"


def kuaisu(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    kuaisu(lists, low, left - 1)
    kuaisu(lists, left + 1, high)
    return lists


