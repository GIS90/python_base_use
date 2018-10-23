



from pysnmp.hlapi import *


print SnmpEngine()


print CommunityData('public',mpModel=0)

print CommunityData('public',mpModel=1)



g=getCmd(SnmpEngine(),
         CommunityData('public'),
         UdpTransportTarget(('demo.snmplabs.com'),161)

)
