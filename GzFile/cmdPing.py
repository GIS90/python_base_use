# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: cmdPing.py
@time: 2016/9/22 17:52
@describe: 
@remark: 
------------------------------------------------
"""

import subprocess

ip = "192.168.2.163"
cmd = "ping %s" % ip
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print p.stdout.read().decode("gbk")


