# -*- coding: utf-8 -*-

# 处理硬盘相关的类和操作
import os
from Define import *
from collections import namedtuple
from Util import *
from SNMPImpl import *
import SSHClient
import re

PARTITION_INFO = namedtuple("PARTITION_INFO", "driver total used free percent")
FORMAT_CONSTANTS = {"GB": 1073741824,
                    "MB": 1048576,
                    "KB": 1024}

DEFAULT_CLUSTER_SIZE = 4096
DEFAULT_GB_SIZE = 1024 * 1024 * 1024
LINUX_DEFAULT_MONITOR_PARTITION = ["/", "/home"]
WINDOWS_DEFAULT_SKIP_PARTITION = ['physical memory', "virtual memory", "memory buffers", "cached memory"]

oidList = {'diskOid': '.1.3.6.1.2.1.25.2.1.4',
           'storageType': '.1.3.6.1.2.1.25.2.3.1.2',
           'diskLabel': '.1.3.6.1.2.1.25.2.3.1.3',
           'allCluster': '.1.3.6.1.2.1.25.2.3.1.5',
           'useCluster': '.1.3.6.1.2.1.25.2.3.1.6'}


def getLocalHDUsage(pathName, sizeFormat="GB"):
    """
    获取本地磁盘空间使用情况
    Args:
        pathName 磁盘盘符, 如果不小心输入的是一个具体的目录，也会尝试根据目录信息猜测正确的磁盘信息
        sizeFormat 为一个字符串，表示返回的数据的单位, 不区分大小写
        Returns:
            tuple = (boolean, full size, free size)
            其中 fullsize 和 freesize的单位根据传入的值来定
        Raises:
            None
            :param sizeFormat:
            :param pathName:
    """
    if not os.path.exists(pathName):
        msg = "getLocalHDUsage the path doesn't exist " + pathName
        raise Exception(msg)
    assert isinstance(pathName, basestring)
    assert isinstance(sizeFormat, basestring)
    sizeFormat = sizeFormat.upper()
    assert sizeFormat in FORMAT_CONSTANTS
    pathName = pathName.upper()
    if platform.system() == 'Windows':
        import ctypes
        driverList = __listPartitionsOnWindows()
        for driver in driverList:
            driver = driver.upper()
            if pathName.startswith(driver):
                driver += ":"
                driver += os.sep
                return __getLocalDriverInfoOnWindows(driver, sizeFormat)
    else:
        return __getLocalDriverInfoOnLinux(pathName, sizeFormat)


def __getRealPartitionList(pListFromSNMP):
    """
    :param pListFromSNMP: 从SNMP的消息中获取到的分区列表，这里面可能不全是硬盘分区，可能有光驱、软驱、虚拟分区等信息，需要过滤掉
    :return:
    """
    assert isinstance(pListFromSNMP, list)
    pList = [item[1] for item in pListFromSNMP]
    retList = []
    for p in pList:
        # 含有A:\\的是软驱
        if p.strip().lower().startswith('a:\\'):
            continue
        # Linux下的无关的分区信息
        elif p.strip().lower() in WINDOWS_DEFAULT_SKIP_PARTITION:
            continue
        # Windows下的Label信息
        elif p.lower().find("label") != -1:
            retList.append(p[0:p.lower().find('label')])
        # Linux下的卷标信息
        elif p.lower() in LINUX_DEFAULT_MONITOR_PARTITION:
            retList.append(p[0:p.lower().find('label')])
        else:
            continue
    return retList


def __getTotalAndUsedSpaceFromSNMP(pList, pTotalList, pUsedList):
    """
    通过SNMP
    :param pList: 通过
    :param pTotalList:
    :param pUsedList:
    :return:
    """
    assert isinstance(pList, list)
    pList = [item[1] for item in pList]
    retList = []
    for index, p in enumerate(pList):
        # 含有A:\\的是软驱
        if p.strip().lower().startswith('a:\\'):
            continue
        # Linux下的无关的分区信息
        elif p.strip().lower() in WINDOWS_DEFAULT_SKIP_PARTITION:
            continue
        # Windows下的Label信息 Linux下的卷标信息
        elif p.lower().find("label") != -1 or (p.lower() in LINUX_DEFAULT_MONITOR_PARTITION):
            try:
                labelIndex = p.lower().find('label')
                # windows platform
                if -1 != labelIndex:
                    name = p[0:p.lower().find('label')]
                else:
                    name = p
                total = float(pTotalList[index][1]) * DEFAULT_CLUSTER_SIZE / float(DEFAULT_GB_SIZE)
                total = float("%.1f" % total)
                used = float(pUsedList[index][1]) * DEFAULT_CLUSTER_SIZE / float(DEFAULT_GB_SIZE)
                used = float("%.1f" % used)
                free = total - used
                free = float("%.1f" % free)
                percent = float("%.1f" % (float(used) / float(total) * 100) if total else 0)
                # print name, total, used
                # continue
                partitionInfo = PARTITION_INFO(name, total, used, free, percent)
                retList.append(partitionInfo)
            except Exception as e:
                continue
        else:
            continue
    return retList


def getRemoteHDUsageBySNMP(ip, gen='agent', comm='public', ver=1, port=161, Cc=False):
    """
    通过SNMP协议获取远端机器的硬盘信息：
        gen：代理设置，默认为agent
        comm：远端SNMP的社区名称，默认为public
        ver：使用的SNMP协议版本，默认是1
        port：SNMP端口号，默认161
        :param Cc:
        :param port:
        :param ver:
        :param comm:
        :param gen:
        :param ip: 远端机器的ip地址
        :returns boolean, errMsg, {}
        成功则返回boolean表示成功还是失败
        errMsg表示错误原因
        {}表示结果
    """
    num = 0
    diskUsePercent = []
    diskLabel = []
    partitions = snmpWalk(ip, SNMPWalkType.DISK_LABEL, gen, comm, ver, port, Cc)
    # 注意,正常的算法为每个分区或卷标的大小=簇的大小(默认4096字节)*簇的个数，使用空间算法类似，簇的大小根据设备的不同而有区别，比如是否为硬盘
    # 或光驱或软驱等簇的值略有不同，本算法只针对硬盘的进行计算，其他的值需要调整下脚本代码
    # Linux的分区还会包含一些iNode等信息，因此跟实际值稍微有差距，但差距不大，Windows基本上是准的
    allSize = snmpWalk(ip, SNMPWalkType.DISK_ALL_CLUSTER, gen, comm, ver, port, Cc)
    usedSize = snmpWalk(ip, SNMPWalkType.USED_CLUSTER, gen, comm, ver, port, Cc)
    return __getTotalAndUsedSpaceFromSNMP(partitions, allSize, usedSize)


def convertSize(inputStr):
    assert isinstance(inputStr, basestring)
    if inputStr.endswith("K"):
        GBValue = float(inputStr.rstrip("K")) / (1024.0 * 1024.0)
        return float("%.3f" % GBValue)
    elif inputStr.endswith("M"):
        GBValue = float(inputStr.rstrip("M")) / 1024.0
        return float("%.3f" % GBValue)
    elif inputStr.endswith("G"):
        GBValue = float(inputStr.rstrip("G"))
        return float("%.1f" % GBValue)


def __getPartitionInfoFromInputLine(diskInfo):
    if len(diskInfo) != 6:
        return None
    p = diskInfo[-1]
    total = diskInfo[1]


def getRemoteHDUsageBySSH(ip, user, passWord, port=22):
    """
    通过SSH协议获取远端机器的硬盘信息：
    :param port: 端口
    :param passWord: user对应的密码
    :param ip: 远端机器的ip地址
    :param user:  远端机器上的用户名
    """
    conn = SSHClient.SSHClient(ip, user, passWord, port)
    state, _ = conn.connect()
    if not state:
        warnMsg = "getRemoteHDUsageBySSH the remote server could not be connected"
        return False, warnMsg, {}
    retval = []
    result = conn.runShellCmd('df -h')
    conn.close()
    resultList = re.split(r'\n', result[1])
    resultList = resultList[1:]
    for result in resultList:
        diskInfo = re.split(r'\s+', result)
        if len(diskInfo) != 6:
            Log.debug("getRemoteHDUsageBySSH the HDStorage info seems is not correct, skip it " + str(diskInfo))
            continue
        # driver total used free percent
        driverInfo = diskInfo[-1]
        total = convertSize(diskInfo[1])
        used = convertSize(diskInfo[2])
        free = convertSize(diskInfo[3])
        percent = "%.1f" % (int(diskInfo[4].rstrip("%")))
        p = PARTITION_INFO(driverInfo, total, used, free, percent)
        retval.append(p)
    conn.close()
    return retval


def __getLocalDriverInfoOnLinux(pathName, sizeFormat):
    """
    通过os模块的statvfs获取Linux主机本地硬盘信息：
    pathName：硬盘的挂载点
    sizeFormat：返回的硬盘容量的数据格式（GB、MB、KB）
    """
    assert isinstance(sizeFormat, basestring)
    assert os.path.exists(pathName)
    sizeFormat = sizeFormat.upper()
    assert sizeFormat in FORMAT_CONSTANTS
    st = os.statvfs(pathName)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    freeSpace = free / FORMAT_CONSTANTS[sizeFormat]
    totalSpace = total / FORMAT_CONSTANTS[sizeFormat]
    usedSpace = used / FORMAT_CONSTANTS[sizeFormat]
    usePercent = float(usedSpace / totalSpace)
    return freeSpace, totalSpace, usedSpace, usePercent


def __getLocalDriverInfoOnWindows(driverName, sizeFormat):
    import ctypes
    _, totalBytes, freeBytes = ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong()
    if sys.version_info >= (3,) or isinstance(driverName, unicode):
        fun = ctypes.windll.kernel32.GetDiskFreeSpaceExW
    else:
        fun = ctypes.windll.kernel32.GetDiskFreeSpaceExA
    ret = fun(driverName, ctypes.byref(_), ctypes.byref(totalBytes), ctypes.byref(freeBytes))
    if ret == 0:
        raise ctypes.WinError()
    freeSize = float(freeBytes.value / FORMAT_CONSTANTS[sizeFormat])
    totalSize = float(totalBytes.value / FORMAT_CONSTANTS[sizeFormat])
    usedSize = totalSize - freeSize
    percent = "%.3f" % (usedSize / totalSize)
    return totalSize, freeSize, float(percent)


def __listPartitionsOnWindows():
    import ctypes
    import string
    driverList = []
    driverBitMask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if driverBitMask & 1:
            driverList.append(letter)
        driverBitMask >>= 1
    return driverList
