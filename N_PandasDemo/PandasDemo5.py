# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import numpy as np
import pandas as pd


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/9"

# 拼接
# s = pd.Series(['a', 'b', 'c'])
# print s.str.cat(sep=',')

# 分割
s = pd.Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'])
# print s.str.split('_')
# print s.str.split('_', -1)
#
# # 获取
# print s.str.get(0)
# print s.str.join('-')

# 包含
print s.str.contains('d')
print s.replace('_', '&')
print s.str.replace('_', '&')
