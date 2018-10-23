# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/18'
"""
import numpy as np
import pandas as pd


s = pd.Series(np.random.randint(1, 5, size=10))
print s
print s.value_counts()
print s.count()
print s.mean()







