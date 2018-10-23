# -*- coding: utf-8 -*-
from TCPServer import TCPServer
from SocketServer import ThreadingTCPServer
from ConfigHandler import *
from SQLHandler import SQLHandler


def main():
    url, user, password = getCfgItems()
    SQLHandler.setConnectInfo(url, user, password)
    if not SQLHandler().testCheck():
        raise Exception("connect to DB failed")
    print "connect to server success"
    sr = ThreadingTCPServer(("", 6688), TCPServer)
    sr.allow_reuse_address = True
    sr.serve_forever()


if __name__ == '__main__':
    main()