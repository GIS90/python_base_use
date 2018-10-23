# -*- coding: utf-8 -*-

from ColorPrint import *
from ArcServerManager import *
from SendMsg import *

if __name__ == '__main__':
    ip = 'localhost'
    port = 6080
    ServerObj = ArcServerManager(ip, port)
    ServersList = ServerObj.getServersList()
    if ServersList != -1:
        InspectResult = ServerObj.inspectServers(ServersList)
        for ServerStatus in InspectResult:
            if ServerStatus[1] == 200:
                pass
            else:
                title = '地图服务异常'.decode('utf-8')
                msg = ''
                SNMPManage.sendMessage(title, msg)
                printGreen(msg)
    else:
        print ''