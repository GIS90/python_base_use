# -*- coding: utf-8 -*-
from SocketServer import ThreadingTCPServer
from MyServer import TCPServer


def main():
    sr = ThreadingTCPServer(("", 40000), TCPServer)
    sr.allow_reuse_address = True
    sr.serve_forever()


if __name__ == '__main__':
    main()
