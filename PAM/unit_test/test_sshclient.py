# -*- coding: utf-8 -*-

import unittest
from core.SSHClient import *
from unittest import *
import paramiko
import re

# class test_sshclient(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def test_ssh(self):
#         a = SSHClient("127.0.0.1", "root", "test")
#         state, _ = a.connect()
#         assert state
#         print "connect success"
#
#         a.isProgramAlive("python")
#         a.startProgramInBackend("python /tmp/t1.py")
#         result, msg = a.runShellCmd("pwd")
#         assert result
#         print "run shell cmd result " + msg
#         result, msg = a.runInteractiveCmd("ifconfig")
#         assert result
#         print "run interactive cmd " + msg
#         a.close()
#
# if __name__ == '__main__':
#     unittest.main()


diskusepercent=[]
diskmounted=[]
conn=SSHClient('192.168.2.200','root','1qaz@WSX')
result=conn.runShellCmd('df -h')
a=re.split(r'\n',result[1])
a=a[1:]
for b in a:
    c=re.split(r'\s+',b)
    diskusepercent.append(c[-2])
    diskmounted.append(c[-1])
dic=dict(zip(diskmounted,diskusepercent))
print(dic['/'])