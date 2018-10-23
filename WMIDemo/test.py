#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import checkWinInfos
import wmi


c=checkWinInfos.WinInfos('192.168.2.158','administrator','0')

print c.getCpuInfo()
print c.getMemoryInfo()
print c.getDiskInfo()
print c.getRunningProcess()


w=wmi.WMI('127.0.0.1')
for p in w.Win32_Process():
    print p.name
