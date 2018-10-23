# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: strlog_demo.py
@time: 2016/10/10 11:38
@describe: 
@remark: 
------------------------------------------------
"""

from structlog import get_logger


log = get_logger()


def virw(request):
    user_agent = request.get("HTP_USER_AGENT", "UBKNOW")
    PEER_IP = request.client_addr
