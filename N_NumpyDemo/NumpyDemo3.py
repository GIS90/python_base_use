# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/3/29'
"""

import numpy as np

arr = np.arange(12).reshape(3, 4)
print arr
print arr.sum(axis=0)
print arr.sum(axis=1)





