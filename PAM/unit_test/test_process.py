# -*- coding: utf-8 -*-

from core.Process import *
#
# checkProcessResult = snmpWalk('192.168.2.198',14)
# pidList = []
# processList = []
# for data in checkProcessResult:
#     pid,process = data
#     pid = pid.split('.')[-1]
#     pidList.append(pid)
#     processList.append(process)
# pidProcess = dict(zip(pidList,processList))
#
# checkCmdLineResult = snmpWalk('192.168.2.198',13)
# cmdPidList = []
# cmdProcessList = []
# for data in checkCmdLineResult:
#     cmdPid,cmdLine = data
#     cmdPid = cmdPid.split('.')[-1]
#     cmdPidList.append(cmdPid)
#     cmdProcessList.append(cmdLine)
#
# checkProcessStatResult = snmpWalk('192.168.2.198',15)
# statPidList = []
# psStatList = []
# for data in checkProcessStatResult:
#     statPid,psStat = data
#     statPid = statPid.split('.')[-1]
#     statPidList.append(statPid)
#     psStatList.append(psStat)
# pidStat = dict(zip(statPidList,psStatList))
#
# processList = []
# pidList = []
# psStatList = []
# for pid in cmdPidList:
#     if pid in pidProcess and pid in pidStat:
#         processList.append(pidProcess[pid])
#         pidList.append(pid)
#         psStatList.append(pidStat[pid])
# cmdList = []
# for index,process in enumerate(processList):
#     #cmdTotal = pidList[index] + ' ' +  processList[index] + ' ' + cmdProcessList[index]
#     # cmdTotal = namedtuple("PROCESS_INFO", "pid ps cmd")
#     # a = PROCESS_INFO("living", 12, "hello", "male", "coder")
#     pid = int(pidList[index])
#     cmdTotal = PROCESS_INFO(pid, process.lower(), cmdProcessList[index].lower(), int(psStatList[index]))
#     cmdList.append(cmdTotal)
# for cmd in cmdList:
#     print cmd
#
# print cmdList[0].pid

test = isRemoteProcessAliveBySNMP('192.168.2.200','public', 161, 'ibus-engine-pin','--ibus')
print test
test1 = isRemoteProcessAliveBySNMP('192.168.2.200','public', 161, 'abc','-dsdd')
print test1