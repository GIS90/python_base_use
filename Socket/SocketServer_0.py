# coding:utf-8


import socket


HOST = ''
PORT = 5432
BUFSIZE = 1024 * 1024
ADDR = (HOST, PORT)
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.bind(ADDR)
sock.listen(2)
print 'Waiting For Connecting......'
socektTcpClient, addr = sock.accept()
while True:

    try:
        revcData = socektTcpClient.recv(BUFSIZE)
        print revcData
    except Exception as e:
        print e.message
        socektTcpClient.close()
        break
    # if revcData:
    #     msg = 'Response data.'
    #     print
        # with open("test.txt", "w") as f:
        #     f.write(revcData)
        # sock.sendall(msg.decode('utf-8'))
    # s = 'Hi,you send me :[%s] %s' % (ctime(), revcData.decode('utf8'))
    # socektTcpClient.send(s.encode('utf8'))
    # print ctime() + 'Client : ' + str(revcData.decode('utf8'))

sock.close()
