#coding:utf-8


from pysnmp.entity.rfc3413.oneliner import cmdgen


class snmpOIDList():
    sysBaseInfo='.1.3.6.1.2.1.1.1.0'
    sysSoftwareList='.1.3.6.1.2.1.25.6.3.1.2'
    sysProcessList='.1.3.6.1.2.1.25.4.2.1.2'

class getCompInfoToSNMP():

    def snmpGet(self,ip,port,community,oid):
        assert isinstance(ip,basestring)
        assert isinstance(community,basestring)
        assert isinstance(oid,basestring)
        retList = []
        communityData = cmdgen.CommunityData(community)
        udpTarget = cmdgen.UdpTransportTarget((ip, port))
        oid = oid
        cg=cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cg.getCmd(communityData,
                                                                       udpTarget,
                                                                       oid)
        if not varBinds:
            return []
        for var in varBinds:
            retList.append(var)
        return "\n".join(retList)
    def snmpWalk(self,ip, port, oid,gen='agent', community='public', ver=1):
        assert isinstance(ip,basestring)
        assert isinstance(community,basestring)
        assert isinstance(oid,basestring)
        retList = []
        communityData = cmdgen.CommunityData(gen, community, ver,)
        udpTarget = cmdgen.UdpTransportTarget((ip, port))
        oid = oid
        cg=cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cg.nextCmd(communityData,
                                                                       udpTarget,
                                                                       oid)
        if not varBinds:
            return []
        for var in varBinds:
            retList.append(var)
        return "\n".join(retList)


