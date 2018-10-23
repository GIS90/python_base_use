#coding:utf-8


from pysnmp.entity.rfc3413.oneliner import cmdgen

class SnmpGetTpyeOid(object):

    #获取系统基本信息
    SysDesc = '.1.3.6.1.2.1.1.1.0'
    #系统联系人
    SysContact = '.1.3.6.1.2.1.1.4.0'
    #监控时间
    SysUptime = '.1.3.6.1.2.1.1.3.0'
    #获取机器名
    SysName = '.1.3.6.1.2.1.1.5.0'
    #系统CPU百分比
    ssCpuUser = '. 1.3.6.1.4.1.2021.11.10.0'
    #空闲CPU百分比
    ssCpuIdle = '. 1.3.6.1.4.1.2021.11.11.0'
    #获取内存大小
    hrMemorySize = '.1.3.6.1.2.1.25.2.2.0'
class SnmpWalkTpyeOid(object):

    #系统运行的进程列表
    HrSWRunName = '.1.3.6.1.2.1.25.4.2.1.2'
    #系统安装的软件列表
    HrSWInstalledName = '.1.3.6.1.2.1.25.6.3.1.2'
    #接口发送和接收的最大IP数据报[BYTE]
    IfMTU = '.1.3.6.1.2.1.2.2.1.4'
    #接口当前带宽[bps]
    IfSpeed = '.1.3.6.1.2.1.2.2.1.5'
    #存储设备编号
    hrStorageIndex = '.1.3.6.1.2.1.25.2.3.1.1'
    #存储设备类型
    hrStorageType = '.1.3.6.1.2.1.25.2.3.1.2'
    #占用率
    hrStorageUsed = '.1.3.6.1.2.1.25.2.3.1.6'
    #簇的大小
    hrStorageAllocationUnits = '.1.3.6.1.2.1.25.2.3.1.4'

def snmpGet(ip, oid, community="public", port=161):
    """
    :param ip:
    :param snmpType:
    :param community:
    :param port:
    :return: 返回 一个包含全部结果的result List
    """
    assert isinstance(ip, basestring)
    assert isinstance(oid, basestring)
    communityData = cmdgen.CommunityData(community)
    snmpTarget = cmdgen.UdpTransportTarget((ip, port))
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(communityData,
                                                                       snmpTarget,
                                                                       oid)
    if not varBinds:
        return []
    return [var.results for var in varBinds]


def snmpWalk(ip, oid, gen='agent', community='public', ver=1, port=161, Cc=False):
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
    assert isinstance(oid, basestring)
    try:
        retList = []
        communityData = cmdgen.CommunityData(gen, community, ver, )
        snmpTarget = cmdgen.UdpTransportTarget((ip, port))
        cmdObj = cmdgen.CommandGenerator()
        if Cc:
            cmdObj.ignoreNonIncreasingOid = True
        errorIndication, errorStatus, errorIndex, varBindTable = cmdObj.nextCmd(communityData, snmpTarget, oid)
        if errorIndication or errorStatus or errorIndex:
            print errorIndication
            return []
        for varBind in varBindTable:
            for name, val in varBind:
                prettyName = name.prettyPrint()
                prettyVal = val._value
                if not prettyName or not prettyVal:
                    continue
                retList.append((prettyName, prettyVal))
        return retList
    except Exception, e:
        print 'Occur Exception : %s'%e.message
        return []
