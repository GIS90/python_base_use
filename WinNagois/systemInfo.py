#coding:utf-8

import platform

'''
获取电脑的System信息
'''

#电脑系统的版本
def getSystemVersion():
    compSystemVersion=platform.platform()
    return compSystemVersion
#电脑系统的位数
def getSystemArch():
    compSystemArch=platform.architecture()
    return compSystemArch
#电脑用户名称
def getUserName():
    compName=platform.node()
    return compName
#获取电脑信息
def getSystemInfo():
    systemInfos=[]
    template = "%30s %30s %20s"
    systemInfos.append(template % ("Version", "Arch", "UserName"))
    systemInfos.append(template % ( getSystemVersion(),
                                    getSystemArch(),
                                    getUserName(),
                                  ))
    return systemInfos

