# -*- coding: utf-8 -*-

from pysnmp.entity.rfc3413.oneliner import cmdgen
from Log import Log
# from flask.ext.bootstrap import Bootstrap


class SNMPGetType(object):
    WINDOWS_CPU = 1
    LINUX_CPU = 2
    WINDOWS_PROGRESS = 3
    LINUX_PROGRESS = 4
    # 网络接口的数目，适用于Linux和windows平台
    NETWORK_INTERFACE_NUMBER = 5

    # 获取机器名称
    SYSTEM_NAME = 6

    DEFINE_END = 7


class SNMPWalkType(object):
    # 获取磁盘的OID 信息
    DISK_OID = 8

    # 磁盘分配单元
    STORAGE_ALLOCATE_UNIT = 9

    # 分区和卷标
    DISK_LABEL = 10

    # 簇信息
    DISK_ALL_CLUSTER = 11

    # 使用的簇
    USED_CLUSTER = 12

    # 进程的参数列表
    PROGRESS_CMDLINE = 13

    # 系统的进程列表
    PROGRESS_LIST = 14

    # 系统的进程状态
    PROGRESS_STATE = 15

    # 枚举的结尾
    DEFINE_END = 16


OID_MAPPING = {
    SNMPGetType.WINDOWS_CPU: ".1.3.6.1.2.1.25.3.3.1.2",
    SNMPGetType.SYSTEM_NAME: ".1.3.6.1.2.1.1.5.0",
    SNMPWalkType.DISK_OID: ".1.3.6.1.2.1.25.2.1.4",
    # 簇的大小，分区的大小为簇的大小 * 簇的数目, 注意Linux下因为有交换分区等，可能获取到的值并非4096， 而是1024
    SNMPWalkType.STORAGE_ALLOCATE_UNIT: ".1.3.6.1.2.1.25.2.3.1.4",

    # 获取网卡数目，适用于Linux和Windows
    SNMPGetType.NETWORK_INTERFACE_NUMBER: ".1.3.6.1.2.1.2.1.0",

    # 存储设备描述，获取卷标
    SNMPWalkType.DISK_LABEL: ".1.3.6.1.2.1.25.2.3.1.3",

    # 簇的数目
    SNMPWalkType.DISK_ALL_CLUSTER: ".1.3.6.1.2.1.25.2.3.1.5",

    # 使用的空间数目 .1.3.6.1.2.1.25.2.3.1.6
    SNMPWalkType.USED_CLUSTER: ".1.3.6.1.2.1.25.2.3.1.6",

    # 进程的参数
    SNMPWalkType.PROGRESS_CMDLINE: ".1.3.6.1.2.1.25.4.2.1.5",

    # 进程列表
    SNMPWalkType.PROGRESS_LIST: ".1.3.6.1.2.1.25.4.2.1.2",

    # 进程状态(此oid的返回值是pid与该进程的状态，其中进程的状态使用数字表示，1代表正在运行，2代表进程的sleep状态，3和4是非正常状态具体含义待查)
    SNMPWalkType.PROGRESS_STATE: ".1.3.6.1.2.1.25.4.2.1.7"
}


def snmpGet(ip, snmpType, community="public", port=161):
    """
    :param ip:
    :param snmpType:
    :param community:
    :param port:
    :return: 返回 一个包含全部结果的result List
    """
    assert isinstance(ip, basestring)
    assert isinstance(snmpType, int)
    assert snmpType in range(SNMPGetType.WINDOWS_CPU, SNMPGetType.DEFINE_END)
    oid = OID_MAPPING[snmpType]
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(cmdgen.CommunityData(community),
                                                                       cmdgen.UdpTransportTarget((ip, port)),
                                                                       oid)
    if not varBinds:
        return []
    return [var.prettyPrint() for var in varBinds]


def snmpWalk(ip, snmpType, gen='agent', community='public', ver=1, port=161, Cc=False):
    """
    :param ip:
    :param snmpType:
    :param gen:
    :param community:
    :param ver:
    :param port:
    :param Cc:
    :return: 结果列表，每个值是一个 key , value的tuple
    """
    assert isinstance(ip, basestring)
    assert isinstance(snmpType, int)
    assert snmpType in range(SNMPWalkType.DISK_OID, SNMPWalkType.DEFINE_END)
    try:
        oid = OID_MAPPING[snmpType]
        retList = []
        communityData = cmdgen.CommunityData(gen, community, ver, )
        snmpTarget = cmdgen.UdpTransportTarget((ip, port))
        cmdObj = cmdgen.CommandGenerator()
        if Cc:
            cmdObj.ignoreNonIncreasingOid = True
        errorIndication, errorStatus, errorIndex, varBindTable = cmdObj.nextCmd(communityData, snmpTarget, oid)
        if errorIndication or errorStatus or errorIndex:
            error = "snmpWalk got error, error is " + str(errorIndication)
            raise Exception(error)
        for varBind in varBindTable:
            for name, val in varBind:
                prettyName = name.prettyPrint()
                prettyVal = val._value
                if not prettyName or not prettyVal:
                    continue
                retList.append((prettyName, prettyVal))
        return retList
    except Exception, e:
        error = "snmpWalk got exception, error is " + str(e)
        raise Exception(error)


if __name__ == '__main__':
    print snmpWalk("192.168.2.200", SNMPWalkType.STORAGE_ALLOCATE_UNIT)
