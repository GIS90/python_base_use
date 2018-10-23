# -*- coding: utf-8 -*-


from SocketServer import BaseRequestHandler, ThreadingTCPServer
import os

"""
    用来接收10.212.129.3，172.26.48.20数据流
    别的机器拒接
"""


class TCPServer(BaseRequestHandler):
    @staticmethod
    def work(dataC, fOpr):
        """
        参数：
                data：接收的数据流
                fOpr：生成文件的路径+名称
                buf：作为判断数据流字节的大小
        :return：返回值为1,代表接收成功，并写成文件
                 返回值为0，代表接收失败，重新发送数据
        """
        dataPath = os.path.abspath(fOpr)
        if os.path.exists(dataPath):
            os.unlink(dataPath)
        try:
            f_d = open(dataPath, 'wb')
            f_d.write(dataC)
            print "Receive data success ."
            f_d.close()
        except Exception as e:
            print 'Work Occur Exception :' + e.message

    def handle(self):
        """
        覆写Handle方法
        """
        cIP = self.client_address[0]
        cPORT = self.client_address[1]
        print '%s : %d Connect Success :' % (cIP, cPORT)
        try:
            curPath = os.getcwd()
            buf = 1024 * 1024
            dataLen = self.request.recv(buf)
            if str(dataLen).isdigit():
                dataContent = self.request.recv(buf)
                print 'Receive Data Length Is : %s' % dataLen
                if int(dataLen) == len(dataContent):
                    revMsg = '1'
                    self.request.sendall(revMsg)
                    print 'Receive %s : %d Data Success .' % (cIP, cPORT)
                    if cIP == '10.212.129.3':
                        size = 50 * 1024
                        fName = 'ResultData.xls'
                        fOpr = os.path.abspath(os.path.join(curPath, fName))
                        self.work(dataContent, fOpr)
                    elif str(cIP) == '172.26.48.20':
                        fName = 'GpsNum.xls'
                        fOpr = os.path.abspath(os.path.join(curPath, fName))
                        self.work(dataContent, fOpr)
                    else:
                        pass
            else:
                revMsg = '0'
                self.request.sendall(revMsg)
                print 'Data Not Correct , ReSend Me .'

        except Exception as e:
            print 'Handle Occur Exception :' + e.message


if __name__ == '__main__':
    """
    设置IP为任意端口
    PORT为10000 + 本机末尾IP
    """
    host = ""
    port = 10253
    addR = (host, port)
    print 'Waite Connect .........'
    server = ThreadingTCPServer(addR, TCPServer)
    server.allow_reuse_address = True
    server.serve_forever()
