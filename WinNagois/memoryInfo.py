#coding:utf-8

import psutil

'''
获取电脑的Memory信息
'''

#定义内存对象
memory=psutil.virtual_memory()
#获取内存使用率
def getMemoryPercent():
    memoryPercent=memory.percent
    return memoryPercent
#获取使用内存大小
def getMemoryUsed():
    memoryUsed=int(memory.used/(1024*1024))
    return memoryUsed
#获取可用内存大小
def getMemoryAvailed():
    memoryAvailed=int(memory.available(1024*1024))
    return memoryAvailed
#获取内存大小
def getMemoryTotal():
    memoryTotal=int(memory.total/(1024*1024))
    return memoryTotal
#获取自由内存大小
def getMemoryFree():
    memoryFree=int(memory.free/(1024*1024))
    return memoryFree
#获取使用内存情况
def getMemorySwap():
    memorySwap=psutil.swap_memory()
    return memorySwap
#获取内存使用信息
def getMemoryInfo():
    memoryInfos=[]
    template = "%10s %10s %10s %10s%%s"
    memoryInfos.append(template % ("Total", "Used", "Free", "Use "))
    memoryInfos.append(template % ( getMemoryTotal(),
                                    getMemoryUsed(),
                                    getMemoryFree(),
                                    getMemoryPercent()
                                  ))
    return memoryInfos