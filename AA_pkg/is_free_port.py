# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: is_free_port.py
@time: 2016/9/12 17:12
@describe: 
@remark: 
------------------------------------------------
"""
import socket


SO_BINDTODEVICE = 25


def get_free_port(iface=None):
    s = socket.socket()
    if iface:
        s.setsockopt(socket.SOL_SOCKET, SO_BINDTODEVICE)

    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()

    return port


print(get_free_port())
