#coding:utf-8

from SnmpServer import *


if __name__=='__main__':
    diskInfos=[]
    template = "%10s %10s %10s %10s %10s%%"
    diskInfos.append(template % ("Device", "Total", "Used", "Free", "Percent"))
    ip = '192.168.2.173'
    oidList={'diskoid':'.1.3.6.1.2.1.25.2.3.1.1',
         'storagetype':'.1.3.6.1.2.1.25.2.3.1.2',
         'disklabel':'.1.3.6.1.2.1.25.2.3.1.3',
         'allcluster':'.1.3.6.1.2.1.25.2.3.1.5',
         'usecluster':'.1.3.6.1.2.1.25.2.3.1.6'}

    diskIds=snmpWalk(ip,oidList['diskoid'])
    diskTotals=snmpWalk(ip,oidList['allcluster'])
    diskUseds=snmpWalk(ip,oidList['usecluster'])
    diskLabels=snmpWalk(ip,oidList['disklabel'])
    print diskTotals
    print diskUseds
    print diskLabels

    for diskLabel in diskLabels:
        device=str(diskLabel).split("'")[3].split('\\')[0]
    for diskTotal in diskTotals:
        total=str(diskTotal).split(",")[1].split(')')[0]
        print int(total)*4/1024/1024
    for diskUsed in diskUseds:
        total=str(diskUsed).split(",")[1].split(')')[0]
        print int(total)*4/1024/1024

