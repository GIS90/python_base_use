# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    server tool be used to received gps data, analyse gps data
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
from SocketServer import BaseRequestHandler
from multiprocessing import Process
from multiprocessing import Queue

# import cx_Oracle

from dbhandler import *
from log import *

SOCKET_DATA_MAX = 1024 * 1024 * 16
FORMMAT = "%Y-%m-%d %H:%M:%S"
queue = Queue.Queue()


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
        print 123
        prod = Producer("producer", queue)
        prod.start()
        print 'p'
        for i in range(1, 5, 1):
            consume_name = "consume_" + str(i)
            cons = Consumer(consume_name, queue)
            print 'c'
            cons.start()


class Producer(Process):
    def __init__(self, name, queue):
        Process.__init__(self)
        self.name = name
        self.worker = queue

    def run(self):
        client = self.client_address
        cur_thread = threading.current_thread().name
        log.info("gps server %s receive %s data" % (cur_thread, client))
        while True:
            gps_data_2 = self.request.recv(SOCKET_DATA_MAX).strip()
            if gps_data_2:
                try:
                    # gps_data_16 = binascii.b2a_hex(gps_data_2)
                    queue.put(gps_data_2)
                except Exception as e:
                    emsg = "%s is break off gps server: %s" % (client, e.message)
                    log.error(emsg)
                    continue

    def show(self):
        pass


class Consumer(Process):
    def __init__(self, name, queue):
        Process.__init__(self)
        self.name = name
        self.worker = queue

    def run(self):

        host, port, user, password, database = get_db_config()
        gps_table = get_gps_table_config()
        try:
            dbhandle = DBHandler(host=host,
                                 port=port,
                                 user=user,
                                 password=password,
                                 database=database)
            dbhandle.open()
            emsg = "Consumer run %s dbhandler is open" % self.name
            log.info(emsg)
        except Exception as e:
            emsg = "Consumer run %s dbhandler open is error: %s" % (self.name, e.message)
            log.error(emsg)
        # try:
        #     self.oracleConn = cx_Oracle.connect('kakou/qtjy2012@192.168.1.13/kakou')
        #     self.oracleCursor = self.oracleConn.cursor()
        #     log.info('oracle connect successful')
        # except Exception, e:
        #     log.error('oracle connect fail')
        while True:
            try:
                cur_time = datetime.now()
                gps_data_16 = self.worker.get(1, 20)
                dataList = gps_data_16.split('7e')
                for data in dataList:
                    print data
                    if len(data) > 10:
                        data = '7e' + data + '7e'
                        oracleValue = Consumer.gps_parse(data, cur_time)
                        value = str(oracleValue)
                        if int(value.split(',')[-1][:-1]) < 3000000 and int(value.split(',')[-3]) < 360:
                            if float(value.split(',')[2]) < 120:
                                continue
                            insert_values = "insert into %s values %s ;" % (gps_table, value)

                            dbhandle.insert(insert_values)
                            # self.oracleInsert(oracleValue)
                            log.info(u"数据入库成功")
            except ValueError as e:
                continue
            except Exception as e:
                continue

    @staticmethod
    def gps_parse(data, cur_time):
        assert isinstance(data, basestring)
        dataTime = ''
        terminalId = data[15:22]
        state = bin(int(data[34:42], 16))
        lat = int(data[42:50], 16) * 0.0001 / 60
        lon = int(data[50:58], 16) * 0.0001 / 60
        speed = int(data[58:62], 16) * 0.1
        direct = int(data[62:64], 16) * 2
        time = bin(int(data[64:76], 16))
        state = state[2:]
        time = time[2:]
        stateAddZero = 32 - len(state)
        timeAddZero = 48 - len(time)
        for j in range(stateAddZero):
            state = '0' + state
        for k in range(timeAddZero):
            time = '0' + time
        for i in range(0, 48, 4):
            dataTime += str(int(time[i:i + 4], 2))
        # state = state[9]
        state = 1  # 由于当前新的GPS源发来的数据解析出来状态值都是0（空车），不参与计算，所以此处暂时强制赋值为1
        gps_time = datetime.strptime(dataTime, '%y%m%d%H%M%S')
        delays = abs(int((cur_time - gps_time).total_seconds()))
        return terminalId, str(gps_time), lon, lat, speed, direct, state, delays
