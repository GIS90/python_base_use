# -*- coding: utf-8 -*-


def test(msg):
    print msg
    import socket
    HOST = '192.168.2.136'
    PORT = 6688
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(msg)
    data = s.recv(1024)
    s.close()
    print 'Received', repr(data)


if __name__ == '__main__':
    m = [
        ("link5m", 2),
        ("mainroad15m", 3),
    ]
    for n, v in m:
        msg = '{"dataType" :%d,"startTime":"2016-02-24 10:00:00","endTime":"2016-02-24 11:00:00"}' % v
        test(msg)