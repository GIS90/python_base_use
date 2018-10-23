# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/29'
"""

import geocoder
g = geocoder.baidu('中国', key='<API KEY>')
print g.latlng