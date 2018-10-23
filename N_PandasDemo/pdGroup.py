# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/18'
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'para', 'var'],
    'B': [1, 2, 3, 4],
    'C': np.random.randn(4)
})
print df

print df.groupby('B').sum()




