#coding:utf-8

import psutil
import os

'''
获取电脑的CPU信息
'''

#cpu的个数
def getcpuCount():
    cpuCount=psutil.cpu_count()
    return cpuCount
#运行的cpu个数
def getcpuCountLogical():
    cpuCount_logical=psutil.cpu_count(logical=False)
    return cpuCount_logical
#cpu使用率
def getcpuPercent():
    cpuPercent=psutil.cpu_percent(interval=1)
    return cpuPercent
#cpu使用量
def getcpuTimes():
    cpuTimes=psutil.cpu_times(percpu=False)
    return cpuTimes
#cpu的User使用量
def getcpuUser():
    cputimes=str(getcpuTimes())
    cputimesLeft=cputimes.split('(')[0]
    cputimesRight=cputimes.split('(')[1]
    result=cputimesRight.split(',')
    r=(result[0].split('=')[1]).split('.')[0]
    return r
#cpu的System使用量
def getcpuSystem():
    cputimes=str(getcpuTimes())
    cputimesLeft=cputimes.split('(')[0]
    cputimesRight=cputimes.split('(')[1]
    result=cputimesRight.split(',')
    r=(result[1].split('=')[1]).split('.')[0]
    return r
#cpu的Idle使用量
def getcpuIdle():
    cputimes=str(getcpuTimes())
    cputimesLeft=cputimes.split('(')[0]
    cputimesRight=cputimes.split('(')[1]
    result=cputimesRight.split(',')
    r=(result[2].split('=')[1]).split('.')[0]
    return r
#获取cpu总量
def getcpuTotal():
    return int(getcpuIdle())+int(getcpuSystem())+int(getcpuUser())
#获取内存使用信息
def getCpuInfo():
    cpuInfos=[]
    template = "%12s %12s %12s %12s %12s %12s %12s%%"
    cpuInfos.append(template % ("cpuCount", "cpuCLog", "cpuUser" , "cpuSystem", "cpuIdle", "cpuTotal", "cpuPer"))
    cpuInfos.append(template % (getcpuCount(),
                                getcpuCountLogical(),
                                getcpuUser(),
                                getcpuSystem(),
                                getcpuIdle(),
                                getcpuTotal(),
                                getcpuPercent()
                                  ))
    return cpuInfos