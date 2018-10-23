# -*- coding: utf-8 -*-


from SocketServer import BaseRequestHandler
from DBHand import *
from AnlyConfigFile import *


class TCPServer(BaseRequestHandler):
    """
    继承BaseRequestHandler类，覆写handle方法
    """
    def handle(self):
        """
        覆写Handle方法
        """
        ClientIP = self.client_address[0]
        ClientPORT = self.client_address[1]
        print '%s : %d Connect Success :' % (ClientIP, ClientPORT)
        try:
            buf = 1024 * 1024
            data = self.request.recv(buf)
            print 'Receive Data Length Is : %s' % len(data)
            if data:
                revMsg = '1'
                self.request.sendall(revMsg)
                print 'Receive %s : %d Data Success .' % (ClientIP, ClientPORT)
                self.work(data)
            else:
                revMsg = '0'
                self.request.sendall(revMsg)
                print 'Data Not Correct , ReSend Me .'
        except Exception as handleE:
            info = 'TCPServer Handle Occur Exception : %s ' % str(handleE.message)
            Log.debug(info.decode('utf-8'))

    @staticmethod
    def work(data):
        """
        数据流处理的方法
        :param data: sql语句，插入成功返回条数
        :return: 无
        """
        db = DBHand(DB_TYPE, DB_SERVER, DB_PORT, DB_DB, DB_UID, DB_PWD)
        try:
            if db.open():
                rlt = db.handle(data)
                print 'Connect DB Success , Insert DB Nums Is %d' % rlt if rlt else 'Insert DB is Failure'
            else:
                print 'Connect DB Failure .'
        except Exception as workE:
            info = 'TCPServer work Occur Exception : %s ' % str(workE.message)
            Log.debug(info.decode('utf-8'))
        finally:
            db.close()


