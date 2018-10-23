#coding:utf-8


import psutil
import platform
import os



#ComputeInfo

# comSystemVersion=platform.platform()
# comSystemArch=platform.architecture()
# comName=platform.node()
#
# print platform.system()
# print 'Computer System Information :'
# print 'Current Computer System Version Is %s .'%comSystemVersion
# print 'Current Computer System Architecture Is %s .'%str(comSystemArch)
# print 'Current Computer System UserName Is %s .'%comName
#
#

#CPU--------------------------------------------------------------
#获取cpu的个数
# cpuCount=psutil.cpu_count()
# #获取运行的cpu个数
# cpuCount_logical=psutil.cpu_count(logical=False)
# #获取cpu占用率
# cpuPercent=psutil.cpu_percent(interval=1)
#
#
#
# cputimes=str(psutil.cpu_times(percpu=False))
# cputimesLeft=cputimes.split('(')[0]
# cputimesRight=cputimes.split('(')[1]
# result=cputimesRight.split(',')
# print result[0]
# print psutil.cpu_times()
# print 'Computer Cpu Information :'
# print 'Localhost Cpu Count : %s .'%cpuCount
# print 'Localhost Working Cpu Count : %s .'%cpuCount_logical
# print 'Localhost Working Cpu Percent : %.2f %%.'%cpuPercent
#
# # Memory-----------------------------------------------------------
# #获取内存情况
# memory=psutil.virtual_memory()
#
# print 'Computer Memory Information :'
# print 'Localhost Working Memory Percent : %.2f %%.'%memory.percent
# print 'Localhost Used Memory : %d M.'%int(memory.used/(1024*1024))
# print 'Localhost Total Memory : %d M.'%int(memory.total/(1024*1024))
#
# # Process
# #获取后台运行的进程
# ProcessIds=psutil.pids()
# print type(ProcessIds)
# for id in ProcessIds:
#     process=psutil.Process(id)
#     proName=process.name()
   # print 'Working Processing Exe Is : %s.'%proName





#Disk--------------------------
disks=psutil.disk_partitions()

names=[]
for disk in disks:

    print disk
    if os.name == 'nt'and ('cdrom' in disk.opts or disk.fstype == ''):
        continue

    print disk.device
    print psutil.disk_usage(disk.device)
    names.append(disk.device)

print names







