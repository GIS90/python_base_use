# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import numpy as np

arr1 = np.arange(0, 60, 10).reshape(-1, 1)
arr2 = np.arange(0, 5)
print arr1.shape, arr2.shape
c = arr1 + arr2

# a = arr2.repeat(6, axis=0)
# print a
# x, y = np.ogrid[0:5, 0:5]
# print x, y
#
# a = np.arange(6).reshape(2, 3)
# b = np.arange(6, 12).reshape(3, 2)
# c = np.dot(a, b)
# print c

a = np.arange(0, 12).reshape(3, 4)
a.tofile("array.txt")

