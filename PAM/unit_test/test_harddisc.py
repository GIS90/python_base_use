# -*- coding: utf-8 -*-

__author__ = 'tsnav-yangyn'

from core.HDStorage import getRemoteHDUsageBySNMP, getRemoteHDUsageBySSH
diskUse = getRemoteHDUsageBySNMP('127.0.0.1')
print(diskUse)
# diskUse = getRemoteHDUsageBySSH('192.168.2.200','root','1qaz@WSX')
# print(diskUse)e