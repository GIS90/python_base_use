# -*- coding: utf-8 -*-

# 网络相关的操作和监测
from Log import Log
from Util import isHostOSWindows, isHostOSLinux

import os
import sys
import socket
import struct
import select
import time

ICMP_ECHO_REQUEST = 8


def checksum(srcString):
    sum = 0
    countTo = (len(srcString) / 2) * 2
    count = 0
    while count < countTo:
        thisVal = ord(srcString[count + 1]) * 256 + ord(srcString[count])
        sum += thisVal
        sum &= 0xffffffff
        count += 2

    if countTo < len(srcString):
        sum += ord(srcString[len(srcString) - 1])
        sum &= 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum += sum >> 16
    answer = ~sum
    answer &= 0xffff

    # Swap bytes. Bugger me if I know why.
    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer


def receiveOnePing(my_socket, ID, timeout):
    """
    receive the ping from the socket.
    :param timeout:
    :param my_socket:
    """
    timeLeft = timeout
    while True:
        startedSelect = time.time()
        whatReady = select.select([my_socket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if not whatReady[0]:
            return
        timeReceived = time.time()
        recPacket, addr = my_socket.recvfrom(1024)
        icmpHeader = recPacket[20:28]
        type, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)
        if packetID == ID:
            bytesInDouble = struct.calcsize("d")
            timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
            return timeReceived - timeSent

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return


def sendOnePing(mySocket, dstAddr, ID):
    dstAddr = socket.gethostbyname(dstAddr)

    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    my_checksum = 0

    # Make a dummy heder with a 0 checksum.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
    bytesInDouble = struct.calcsize("d")
    data = (192 - bytesInDouble) * "Q"
    data = struct.pack("d", time.time()) + data

    # Calculate the checksum on the data and the dummy header.
    my_checksum = checksum(header + data)

    # Now that we have the right checksum, we put that in. It's just easier
    # to make up a new header than to stuff it into the dummy.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1)
    packet = header + data
    mySocket.sendto(packet, (dstAddr, 1))


def do_one(dest_addr, timeout):
    """
    Returns either the delay (in seconds) or none on timeout.
    :param timeout:
    :param dest_addr:
    """
    icmp = socket.getprotobyname("icmp")
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    except socket.error, (errno, msg):
        if errno == 1:
            # Operation not permitted
            msg += " - Note that ICMP messages can only be sent from processes"
            raise socket.error(msg)
        raise Exception(msg)
        # raise the original error

    my_ID = os.getpid() & 0xFFFF

    sendOnePing(my_socket, dest_addr, my_ID)
    delay = receiveOnePing(my_socket, my_ID, timeout)

    my_socket.close()
    return delay


def verbose_ping(dest_addr, timeout=2, count=4):
    """
    Send >count< ping to >dest_addr< with the given >timeout< and display
    the result.
    :param count:
    :param timeout:
    :param dest_addr:
    """
    for i in xrange(count):
        print "ping %s..." % dest_addr,
        try:
            delay = do_one(dest_addr, timeout)
        except socket.gaierror, e:
            print "failed. (socket error: '%s')" % e[1]
            break

        if delay is None:
            print "failed. (timeout within %ssec.)" % timeout
        else:
            delay *= 1000
            print "get ping in %0.4fms" % delay
    print


def listNetworkDevices():
    """列出本机所有的网卡设备
    Args:
        None
    Returns:
        如果是成功，
    Raises:
        None.
    """
    import psutil
    print psutil.net_if_addrs()

