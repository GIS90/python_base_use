# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: __init__.py.py
@time: 2016/8/28 15:56
@describe: 
@remark: 
------------------------------------------------
"""

if __name__ == '__main__':
    import collections
    a = ["bt", "zgf", "wgf", "wj", "yj"]
    b = ["白天", "早高峰", "晚高峰", "晚间", "夜间"]
    regular_dict = dict(zip(a, b))
    ordered_dict = collections.OrderedDict(zip(a, b))
    print 'Regular Dict:'
    for k, v in regular_dict.items():
        print k, v
    print 'Ordered Dict:'
    for k, v in ordered_dict.items():
        print k, v

