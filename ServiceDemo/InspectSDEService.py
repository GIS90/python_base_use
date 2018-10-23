# coding:utf-8

import os
import sys
import wmi
import platform
import time
import datetime


class NTSevInspect(object):
    """
    如果是windows系统就进行初始化，否则退出
    init初始化设置要监测的电脑IP，替换localhost即可
    """

    def __init__(self):
        if platform.system() == 'Windows':
            self.c = wmi.WMI('localhost')
        else:
            sys.exit(0)

    def GetSevList(self, SevType='all'):
        """
        利用初始化的wmi.WMI对象进行获取所以服务
        :return: 返回所有的服务名称列表
        """
        ST = ['all', 'stopped', 'running']
        assert SevType.lower() in ST
        SevList = []
        if SevType.lower() == 'all':
            Services = self.c.Win32_Service()
            for s in Services:
                SevList.append(s.Caption)
        elif SevType.lower() == 'stopped':
            Services = self.c.Win32_Service(State="Stopped".decode('utf-8'))
            for s in Services:
                SevList.append(s.Caption)
        elif SevType.lower() == 'running':
            Services = self.c.Win32_Service(State="Running".decode('utf-8'))
            for s in Services:
                SevList.append(s.Caption)
        return SevList

    def Count(self, SevType='all'):
        ST = ['all', 'stopped', 'running']
        assert SevType.lower() in ST
        Count = 0
        if SevType.lower() == 'all':
            AllSev = self.GetSevList()
            for s in AllSev:
                Count += 1
        elif SevType.lower() == 'stopped':
            Services = self.GetSevList(SevType)
            for s in Services:
                Count += 1
        elif SevType.lower() == 'running':
            Services = self.GetSevList(SevType)
            for s in Services:
                Count += 1
        return Count

    def CheckSev(self, checkName):
        Services = self.GetSevList()
        for sv in Services:
            return True if sv == checkName else False


if __name__ == '__main__':

    wsi = NTSevInspect()
    SevType = 'running'
    checkNum = 1
    checkName = 'ArcSde Service(esri_sde)'
    formatterTime = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now()
    dt = now.strftime(formatterTime)

    while True:
        print '%s Start Check Num = %d' % (dt, checkNum)
        Services = wsi.GetSevList(SevType)
        checkNum += 1
        if checkName in Services:
            print '%s is running ....' % checkName
            time.sleep(3600)
