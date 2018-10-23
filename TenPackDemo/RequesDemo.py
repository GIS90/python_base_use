# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: RequesDemo.py
@time: 2016/9/30 15:47
@describe: 
@remark: 
------------------------------------------------
"""

import requests


url = "https://github.com/timeline.json"
#
# r_g = requests.get(url)
# print r_g.text
# r_g.encoding = "ISO-8859-1"
# print r_g.text

# file_handle = open("foo.txt", "r")
# file_handle.seek(2)
# contents = file_handle.read()
# print contents
# print file_handle.tell()

r = requests.get(url, stream=True)
print r.raw
print r.raw.read()
with open("foo.txt", "wb") as fd:
    for chunk in r.iter_content(1):
        fd.write(chunk)
print 1

