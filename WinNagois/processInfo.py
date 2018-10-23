#coding:utf-8

import psutil

'''
获取电脑后台正在运行的Process信息
'''

#定义进程列表
ProcessIds=psutil.pids()
#获取进程的ID列表
def getProcessIdList():
    return ProcessIds
def getgetProcessNameList():
    ProcessNames=[]
    for id in ProcessIds:
        process=psutil.Process(id)
        proName=process.name()
        ProcessNames.append(proName)
    return ProcessNames

