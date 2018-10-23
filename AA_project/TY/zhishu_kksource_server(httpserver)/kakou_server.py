# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    kakou_server be used to receive, analyse, import database about kakou source
    it need run to modify config file that contains server host, server port,
    database host, database port, database user, database password, database default
    kakou folder
    database kakou table

        +--------------+
        |  Run  Server |
        +--------------+
                |
                v
        +------- -----+
        |Recive  Kakou| --<--
        +-------------+       ^
                |             |
                v             |
        +--------------+      ^
        |Analyse Kakou |      |
        +--------------+      |
                |             ^
                v             |
        +--------------+      |
        | Store  Kakou | -->--
        +--------------+

------------------------------------------------
"""
from BaseHTTPServer import HTTPServer

from core.log import *
from core.server import *

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/25"

if __name__ == "__main__":
    server_host, server_port = get_server_config()
    addr = (server_host, server_port)
    msg = "Kakou server %s start run......" % str(addr)
    log.info(msg)
    server = HTTPServer((server_host, server_port), KaKouRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
