
#coding:utf-8



import socket
import struct


HOST = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


buf = s.recvfrom(65565)
src_ip = "%d.%d.%d.%d"%struct.unpack('BBBB', buf[0][12:16])
dest_ip ="%d.%d.%d.%d"%struct.unpack('BBBB', buf[0][16:20])
print src_ip, dest_ip
print s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)