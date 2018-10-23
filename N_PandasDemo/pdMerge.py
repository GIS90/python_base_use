# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/18'
"""
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10, 4))
print df
pi = [df[:3], df[3:7], df[7:]]
print pi
print '---------------------------------------------------------------------------------------'
print pd.concat(pi)

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo1'], 'rval': [3, 4]})
print left
print right
print pd.merge(left, right, on='key')









