# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: judge_net.py
@time: 2016/9/12 16:28
@describe: 
@remark: 
------------------------------------------------
"""

import socket


def is_connected(url):
    try:
        host = socket.gethostbyname(url)
        s = socket.create_connection((host, 80), 2)
        return True
    except Exception as e:
        return False


url = "www.baidu.com"

print is_connected(url)

