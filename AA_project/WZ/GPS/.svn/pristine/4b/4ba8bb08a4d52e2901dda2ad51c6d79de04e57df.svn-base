# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
if __name__ == "__main__":
    import SocketServer
    host = ""
    port = 1990
    addr = (host, port)
    print "Server start"
    server = SocketServer.ThreadingTCPServer(addr, TCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()



