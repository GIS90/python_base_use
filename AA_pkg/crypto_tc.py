# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: crypto_tc.py
@time: 2016/11/23 15:10
@describe: 加密解密test
@remark: 
------------------------------------------------
"""


import base64

ens = base64.encodestring("admin")
des = base64.decodestring(ens)
print ens
print des
