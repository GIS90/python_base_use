#coding:utf-8

import psutil
import os

'''
获取电脑的Disk信息
'''

#定义disk对象
disks=psutil.disk_partitions()
#获取硬盘设备名称列表信息
def getDiskDeviceNamesInfo():
    diskNames=[]
    for disk in disks:
        if os.name == 'nt'and ('cdrom' in disk.opts or disk.fstype == ''):
            continue
        diskNames.append(disk.device)
    return diskNames
#获取每个硬盘的详细信息
def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n
def getDiskInfos():
    diskInfos=[]
    template = "%10s %10s %10s %10s %10s%% %10s"
    diskInfos.append(template % ("Device", "Total", "Used", "Free", "Use ", "Type"))
    disks=psutil.disk_partitions(all=False)
    for disk in disks:
        if os.name == 'nt'and ('cdrom' in disk.opts or disk.fstype == ''):
                continue
        usage = psutil.disk_usage(disk.device)
        diskInfos.append(template % (
            disk.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            usage.percent,
            disk.fstype))
    return diskInfos






