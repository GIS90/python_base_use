# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    gps_server be used to receive, analyse, import database about gps source
    it need run to modify config file that contains server host, server port,
    database host, database port, database user, database password, database default

        +------------+
        | Run Server |
        +------------+
              |
              v
        +------------+
        | Recive GPS | --<--
        +------------+      ^
              |             |
              v             |
        +------------+      ^
        |Analyse GPS |      |
        +------------+      |
              |             ^
              v             |
        +------------+      |
        | Import GPS | -->--
        +------------+

------------------------------------------------
"""
import SocketServer

from core.config import *
from core.server_bk import *


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/7"


# linux下创建守护进程用
def daemon():
    try:
        if not hasattr(os, "fork"):
            log.error("It seems the OS is not linux, we only works on windows")
            return
        pid = os.fork()
        if pid > 0:
            # exit first parent
            sys.exit(0)
    except OSError, e:
        sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
        sys.exit(1)

    # decouple from parent environment
    os.setsid()
    os.umask(0)

    # do second fork
    try:
        pid = os.fork()
        if pid > 0:
            # exit from second parent
            sys.exit(0)
    except OSError, e:
        sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
        sys.exit(1)


if __name__ == "__main__":
    host, port = get_server_config()
    addr = (host, port)
    msg = "GPS Server %s start run......" % str(addr)
    log.info(msg)
    print 'start'
    # daemon()
    server = SocketServer.ThreadingTCPServer(addr, TCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
