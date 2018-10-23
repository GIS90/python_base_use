# -*- coding: utf-8 -*-

from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmpget(ip, port, community, oid):

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(cmdgen.CommunityData(community),
                                                                       cmdgen.UdpTransportTarget((ip, port)),
                                                                       oid)

    if not varBinds:
        return
    for a in varBinds:
        print a

def walk(ip, oid, gen='agent', comm='public', ver=1, port=161, Cc=False):
    nameList = []
    valList = []
    communityData = cmdgen.CommunityData(gen, comm, ver,)
    snmpTarget = cmdgen.UdpTransportTarget((ip, port))
    cmdObj = cmdgen.CommandGenerator()
    if Cc:
        cmdObj.ignoreNonIncreasingOid = True
    errorIndication, errorStatus, errorIndex, varBindTable = cmdObj.nextCmd(communityData, snmpTarget, oid)
    if errorIndication or errorStatus or errorIndex:
        pass
    for varBind in varBindTable:
        for name, val in varBind:
            print name.prettyPrint(), val.prettyPrint()
            nameList.append(name.prettyPrint())
            valList.append(val.prettyPrint())
    return (nameList, valList)


#snmpget("192.168.2.200", 161, "public", ".1.3.6.1.2.1.1.1.0")
# 1.3.6.1.2.1.25.6.3.1.2

#OID_LIST = [".1.3.6.1.2.1.1.1.0",
#            ".1.3.6.1.2.1.2.2.1.5"]
#snmpget("192.168.2.198", 161, "public", ".1.3.6.1.2.1.1.1.0")
#snmpget("192.168.2.198", 161, "public", ".1.3.6.1.2.1.25.2.2.0")
# snmpget("192.168.2.198", 161, "public", ".1.3.6.1.2.1.25.4.2.1")
# 安装的进程列表
#walk("192.168.2.200", ".1.3.6.1.2.1.25.6.3.1.2")
# walk("192.168.2.200", ".1.3.6.1.2.1.25.6.3.1.2")
#walk("192.168.2.200", ".1.3.6.1.2.1.25.4.2.1.2")

# print('linux\nfreecpu')
# snmpget('192.168.2.200',161,'public','.1.3.6.1.4.1.2021.11.11.0')
# print('proocesslist')
# walk('192.168.2.200','.1.3.6.1.2.1.25.4.2.1.2')
# print('processpath')
# walk('192.168.2.200','.1.3.6.1.2.1.25.4.2.1.4')
# print('cmdparameter')
# walk('192.168.2.200','.1.3.6.1.2.1.25.4.2.1.5')
# print('processstate')
# walk('192.168.2.200','.1.3.6.1.2.1.25.4.2.1.7')
# print('storagetype')
# walk('192.168.2.200','.1.3.6.1.2.1.25.2.3.1.2')
# print('storagedesc')
# walk('192.168.2.200','.1.3.6.1.2.1.25.2.3.1.3')
# print('clustersize')
# walk('192.168.2.200','.1.3.6.1.2.1.25.2.3.1.4')
# print('clusternum')
# walk('192.168.2.200','.1.3.6.1.2.1.25.2.3.1.5')
# print('clusterusenum')
# walk('192.168.2.200','.1.3.6.1.2.1.25.2.3.1.6')
#
# print('\n\nwindows\nfreecpu')
# snmpget('192.168.2.198',161,'public','.1.3.6.1.4.1.2021.11.11.0')
# print('proocesslist')
# walk('192.168.2.198','.1.3.6.1.2.1.25.4.2.1.2')
# print('processpath')
# walk('192.168.2.198','.1.3.6.1.2.1.25.4.2.1.4')
# print('cmdparameter')
# walk('192.168.2.198','.1.3.6.1.2.1.25.4.2.1.5')
# print('processstate')
# walk('192.168.2.198','.1.3.6.1.2.1.25.4.2.1.7')
# print('storagetype')
# walk('192.168.2.198','.1.3.6.1.2.1.25.2.3.1.2')
# print('storagedesc')
# walk('192.168.2.198','.1.3.6.1.2.1.25.2.3.1.3')
# print('clustersize')
# walk('192.168.2.198','.1.3.6.1.2.1.25.2.3.1.4')
# print('clusternum')
# walk('192.168.2.185','.1.3.6.1.2.1.25.2.3.1.5')
# print('clusterusenum')
# walk('192.168.2.198','.1.3.6.1.2.1.25.2.3.1.6')
# snmpget('192.168.2.200',161,'public','.1.3.6.1.4.1.2021.4.11.0')