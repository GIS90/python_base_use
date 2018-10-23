# -*- coding: utf-8 -*-

# 进程级别的相关监控

from collections import namedtuple

from SNMPImpl import *

PROCESS_INFO = namedtuple("PROCESS_INFO", "pid ps cmd stat")


def isLocalProcessAliveByPID(pid):
    """
    监测本地的进程是否存活
    Args:
        pid: 进程的PID号
    Returns:
        True为alive, false为不存在
    Raises:
        None
    """
    assert isinstance(pid, int)
    import psutil
    return psutil.pid_exists(pid)


def __removeExeSuffixIfExist(psName):
    assert isinstance(psName, basestring)
    psName = psName.lower()
    if psName.endswith(".exe"):
        return psName.rstrip(".exe")
    else:
        return psName


def __isListEqual(list1, list2):
    assert isinstance(list1, list)
    assert isinstance(list2, list)
    if len(list1) != len(list2):
        return False
    return 0 == cmp(list1, list2)


def __getRemoteProcessList(ip, community, port):
    checkProcessResult = snmpWalk(ip, 14, community=community, port=port)
    checkCmdLineResult = snmpWalk(ip, 13, community=community, port=port)
    checkProcessStatResult = snmpWalk(ip, 15, community=community, port=port)
    if not checkProcessResult or not checkCmdLineResult or not checkProcessStatResult:
        return []
    pidList = []
    processList = []
    try:
        for data in checkProcessResult:
            pid, process = data
            pid = pid.split('.')[-1]
            pidList.append(pid)
            processList.append(process)
        pidProcess = dict(zip(pidList, processList))
        cmdPidList = []
        cmdProcessList = []
        for data in checkCmdLineResult:
            cmdPid, cmdLine = data
            cmdPid = cmdPid.split('.')[-1]
            cmdPidList.append(cmdPid)
            cmdProcessList.append(cmdLine)
        statPidList = []
        psStatList = []
        for data in checkProcessStatResult:
            statPid, psStat = data
            statPid = statPid.split('.')[-1]
            statPidList.append(statPid)
            psStatList.append(psStat)
        pidStat = dict(zip(statPidList, psStatList))
        processList = []
        pidList = []
        psStatList = []
        for pid in cmdPidList:
            if pid in pidProcess and pid in pidStat:
                processList.append(pidProcess[pid])
                pidList.append(pid)
                psStatList.append(pidStat[pid])
        cmdList = []
        for index, process in enumerate(processList):
            pid = int(pidList[index])
            cmdTotal = PROCESS_INFO(pid, process.lower(), cmdProcessList[index].lower(), int(psStatList[index]))
            cmdList.append(cmdTotal)
        return cmdList
    except Exception, e:
        error = '进程列表信息处理失败，错误为：' + str(e)
        raise Exception(error)


def isLocalProcessAliveByName(psName, cmdList=None):
    """
    监测本地的进程是否存活
    Args:
        program: 进程名称
        cmdList: 命令行参数列表
    Returns:
        True为alive, False为No
    Raises:
        None
    """
    import psutil
    assert isinstance(psName, basestring)
    assert isinstance(cmdList, list)
    psName = __removeExeSuffixIfExist(psName)
    cmdList = [item.replace("\\", "/") for item in cmdList]
    cmdList = [item.replace("//", "/") for item in cmdList]
    cmdList = [item.lower() for item in cmdList]
    pidList = psutil.pids()
    for eachPid in pidList:
        p = psutil.Process(eachPid)
        if __removeExeSuffixIfExist(p.name()) != psName:
            continue
        cmdline = p.cmdline()
        if len(cmdline) > 1:
            argList = cmdline[1:]
            argList = [item.lower() for item in argList]
            argList = [item.replace("\\", "/") for item in argList]
            argList = [item.replace("//", "/") for item in argList]
            if not __isListEqual(cmdList, argList):
                continue
            else:
                return True
    return False


def isRemoteProcessAliveBySNMP(ip, community, port, program, cmdList=None):
    program = __removeExeSuffixIfExist(program)
    cmdList = [item.replace("\\", "/") for item in cmdList]
    cmdList = [item.replace("//", "/") for item in cmdList]
    cmdList = [item.lower() for item in cmdList]
    remoteProcessList = __getRemoteProcessList(ip, community, port)
    if remoteProcessList:
        for remoteProcess in remoteProcessList:
            if __removeExeSuffixIfExist(remoteProcess.ps) != program:
                continue
            cmdline = remoteProcess.cmd
            if len(cmdline) > 1:
                if cmdline[0].isspace():
                    cmdline = cmdline[1:]
                argList = [item.replace("\\", "/") for item in cmdline]
                argList = [item.replace("//", "/") for item in argList]
                if not __isListEqual(cmdList, argList):
                    continue
                elif remoteProcess.stat == 1 or remoteProcess.stat == 2:
                    return 0, program + ' ' + ''.join(cmdList) + '进程运行正常', 'stat=' + str(remoteProcess.stat)
                else:
                    return 1, program + ' ' + ''.join(cmdList) + '进程没有运行', 'stat=' + str(remoteProcess.stat)
        return 1, '进程没有找到', '0'
    else:
        error = '没有获取到远程主机进程列表, 主机ip：' + ip
        raise Exception(error)


def isRemoteProcessAliveBySSH(ip, user, password, port, program, cmdList=[]):
    pass


def isRemoteProcessAliveByWindowsRemote(ip, user, secret, program, cmdList):
    pass


if __name__ == '__main__':
    # print isLocalProcessAliveByName("python.exe", ["E:\PAM\Core\Process.py"])
    isRemoteProcessAliveBySNMP("a", 2)
