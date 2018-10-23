# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    this tool be used to
------------------------------------------------
"""
import SocketServer
import codecs
import datetime
import os
import threading
from SocketServer import BaseRequestHandler

SOCKET_DATA_MAX = 16 * 1024 * 1024
FORMMAT = "%Y%m%d%H%M%S"


def __get_cur_folder():
    # if getattr(sys, "frozen", False):
    return os.path.dirname(os.path.abspath(__file__))
    # else:
    #     cur_folder = os.path.dirname(inspect.getfile(inspect.currentframe()))
    #     return os.path.abspath(cur_folder)


_cur_folder = __get_cur_folder()
_gps_file_folder = os.path.abspath(os.path.join(_cur_folder, "liveGPS"))
if not os.path.exists(_gps_file_folder):
    os.makedirs(_gps_file_folder)


class TCPRequestHandler(BaseRequestHandler):
    """
    The RequestHandler class for my server.
    It is instantiated once per connection to the server, and must
    override the handle method to implement communication to the
    client.
    """

    def setup(self):
        BaseRequestHandler.setup(self)

    def handle(self):

        while True:
            try:
                data = self.request.recv(SOCKET_DATA_MAX).strip()
                if data:
                    print data
                    gps_file_name = "gps.dat"
                    gps_file = os.path.join(_gps_file_folder, gps_file_name)
                    gps = codecs.open(gps_file, 'wb', 'utf-8')
                    gps.write(data)
                    gps.close()
            except Exception as e:
                print e.message



if __name__ == "__main__":
    host = ""
    port = 1991
    addr = (host, port)
    print "Server start ......"
    # It use to
    server = SocketServer.ThreadingTCPServer(addr, TCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
