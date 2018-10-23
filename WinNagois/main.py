#coding:utf-8

import cpuInfo
import memoryInfo
import processInfo
import systemInfo
import diskInfo

'''
获取电脑硬盘信息
'''
diskInfos=diskInfo.getDiskInfos()
print '电脑的硬盘信息为：'
for dInfo in diskInfos:
    print dInfo

'''
获取电脑的内存信息
'''
memoryInfos=memoryInfo.getMemoryInfo()
print '电脑的内存信息为：'
for mInfo in memoryInfos:
    print mInfo

'''
获取电脑的CPU信息
'''
cpuInfos=cpuInfo.getCpuInfo()
print '电脑的CPU信息为：'
for cInfo in cpuInfos:
    print cInfo

'''
获取电脑的System信息
'''
systemInfos=systemInfo.getSystemInfo()
print '电脑的System信息为：'
for sInfo in systemInfos:
    print sInfo

'''
获取电脑的Process信息
'''
processInfos=processInfo.getgetProcessNameList()
print '电脑的Process信息为：'
for pInfo in processInfos:
    print pInfo


