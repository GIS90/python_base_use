# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/25'
"""
import wmi

cObj = wmi.WMI(computer='localhost')
Services = cObj.Win32_Service(State="Stopped")
for i in Services:
    # print i.Caption + '-----------------------' + i.State
    if i.State == 'Stopped':
        print i.Caption
        i.StartService()
        print 'success'
        import time

        print i.State
        print '---------------------------------------------------'
Services = cObj.Win32_Service()
for i in Services:
    if i.Caption == 'ArcSde Service(esri_sde)':
        print i.State

