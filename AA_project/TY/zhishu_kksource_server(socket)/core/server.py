# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    server tool be used to received kakou data, analyse kakou data
    and import to mysql database,
    database is only support mysql
    and can expand database in dbhandler file according to demand

demo:

if __name__ == "__main__":
    host = ""
    port = 1990
    addr = (host, port)
    print "Server start"
    server = SocketServer.ThreadingTCPServer(addr, TCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
------------------------------------------------
"""
import datetime
import sys
import json
import threading
from SocketServer import BaseRequestHandler

from config import *
from dbhandler import *
from log import *

SOCKET_DATA_MAX = 1024 * 1024 * 16
FORMMAT = "%Y-%m-%d %H:%M:%S"


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
        """
        run handle
        :return:
        """
        host, port, user, password, database = get_db_config()
        event_table = get_event_table_config()
        event_folder = get_event_folder_config()
        try:
            dbhandle = DBHandler(host=host,
                                 port=port,
                                 user=user,
                                 password=password,
                                 database=database)
            dbhandle.open()
            log.info("TCPRequestHandler handle dbhandler is open")
        except Exception as e:
            emsg = "TCPRequestHandler handle dbhandler open is error: %s" % e.message
            log.error(emsg)
            sys.exit()
        client = self.client_address
        cur_thread = threading.current_thread().name
        log.info("Kakou server %s receive %s data" % (cur_thread, client))

        while True:
            try:
                event_datas = self.request.recv(SOCKET_DATA_MAX).strip()
                print event_datas
                if event_datas:
                    try:
                        value = TCPRequestHandler.event_parse(event_datas)
                        insert_values = "insert into %s values %s;" % (event_table, value)
                        print insert_values
                        dbhandle.insert(insert_values)
                    except Exception as e:
                        emsg = "TCPRequestHandler event data is error: %s" % e.message
                        log.error(emsg)
            except Exception as e:
                continue
        dbhandle.close()

    @staticmethod
    def event_parse(data):
        assert isinstance(data, basestring)
        event = json.loads(data, encoding="utf8")
        hphm = event["body"]["hphm"]
        jgsj = event["body"]["jgsj"]
        cdbh = event["body"]["cdbh"]
        fxbh = event["body"]["fxbh"]
        clsd = event["body"]["clsd"]
        kkmc = event["body"]["kkmc"]
        jdz = event["body"]["jdz"]
        wdz = event["body"]["wdz"]
        dateArray = datetime.datetime.utcfromtimestamp(jgsj / 1000)
        jgsj = dateArray.strftime(FORMMAT)
        value = "('" + hphm + "','" + jgsj + "'," + cdbh + "," + fxbh + "," + clsd + ",'" + kkmc + "'," + jdz + "," + wdz + ")"
        return value
