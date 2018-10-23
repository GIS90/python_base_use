#coding:utf-8

import wmi

class WinInfos(object):
    #wmi对象初始化
    def __init__(self,ipAddress,userName,passWord):
        self.wmiObj=wmi.WMI(
            computer=ipAddress,
            user=userName,
            password=passWord
        )
        self.ipAddress=ipAddress
        #if(userName!='' & passWord!=''):
        self.userName=userName
        self.passWord=passWord
    #获取内存信息
    def getMemoryInfo(self):
        memoryInfo={}
        osObj=self.wmiObj.Win32_OperatingSystem()
        totalMemory=int(osObj[0].TotalVisibleMemorySize)/1024
        freeMemory=int(osObj[0].FreePhysicalMemory)/1024
        workMemory=totalMemory-freeMemory
        memoryPercent=(workMemory*1.0/totalMemory)*100
        memoryInfo['totalMemory']=totalMemory
        memoryInfo['freeMemory']=freeMemory
        memoryInfo['workMemory']=workMemory
        memoryInfo['memoryPercent']='%0.2f %%'%memoryPercent
        return memoryInfo
    #获取cpu信息
    def getCpuInfo(self):
        cpuInfo={}
        cpuPercent=self.wmiObj.Win32_Processor()[0].LoadPercentage
        cpuInfo['cpuPercent']=cpuPercent
        return cpuInfo
    #获取硬盘信息
    #print  "%5s %.2f%% free" %(disk.Caption,100.0 * long(disk.FreeSpace) / long(disk.Size))
    def getDiskInfo(self):
        diskInfo={}
        for disk in self.wmiObj.Win32_LogicalDisk(DriveType=3):
            diskCaption=str(disk.Caption)
            diskPercent="%.1f%% Free" %(100.0*long(disk.FreeSpace)/long(disk.Size))
            diskInfo[diskCaption]=diskPercent
        return diskInfo
    #获取所有运行的进程
    def getRunningProcess(self):
        processInfo={}
        for pro in self.wmiObj.Win32_Process():
            proId=pro.ProcessId
            proName=str(pro.Name)
            processInfo[proId]=proName
        return processInfo
