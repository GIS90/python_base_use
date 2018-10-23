# -*- coding: utf-8 -*-


from SocketServer import BaseRequestHandler, ThreadingTCPServer


class TCPServer(BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(10 * 1024).strip()
                print "receive from [ %s ] : %s" % (self.client_address, data)

                if data:
                    path = r'E:\aaa.xls'
                    f_d = open(path, 'wb')
                    f_d.write(data)
                    f_d.close()
                    msg = raw_input()
                    self.request.sendall(msg)
            except Exception as e:
                print e.message


if __name__ == '__main__':
    host = ""
    port = 4322
    addr = (host, port)
    print 'start'
    server = ThreadingTCPServer(addr, TCPServer)
    server.allow_reuse_address = True
    server.serve_forever()



