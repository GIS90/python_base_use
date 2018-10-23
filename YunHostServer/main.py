# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/11'
"""
from core.YunHostServer import *
from core.AnlyConfigFile import *
from SocketServer import ThreadingTCPServer


def ServerMain():
    ServerHOST = SERVER_IP
    ServerPORT = SERVER_PORT
    ServerADDR = (ServerHOST, ServerPORT)
    print 'Waite Connect .........'
    server = ThreadingTCPServer(ServerADDR, TCPServer)
    server.allow_reuse_address = True
    server.serve_forever()


if __name__ == '__main__':
    """
    此脚本为Server端，从配置文件中获取IP，PORT
    主入口
    """
    ServerMain()
