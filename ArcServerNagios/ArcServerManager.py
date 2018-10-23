# - * - coding: utf-8 - * -

"""
注：
    针对指定的服务器进行ArcGIS Server服务的监控
"""

import urllib2
import urllib
import re
from collections import namedtuple
import execeptionLogging


class ArcServerManager(object):
    def __init__(self, ip, port):
        assert isinstance(ip, basestring)
        assert isinstance(port, int)
        self.ip = ip
        self.port = port

    def getServersList(self):
        Servers = []
        try:
            url = 'http://' + self.ip + ':' + str(self.port) + '/arcgis/rest/services/?f=sitemap'
            request = urllib2.Request(url)
            request.add_header('User-agent', 'Mozilla 5.10')
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            reg = '<loc>(.*?)</loc>'
            pattern = re.compile(reg, re.S)
            results = re.findall(pattern, content)
            for result in results:
                Servers.append(result)
            return Servers
        except Exception as e:
            logType = 'ERROR'
            logInfo = e.message
            execeptionLogging.log(logType, logInfo)
            return -1

    def inspectServers(self, SList):
        ServersStatus = []
        requestCode = namedtuple('requestCode', 'url status')
        for SListURL in SList:
            status = urllib.urlopen(SListURL).getcode()
            ServersStatus.append(requestCode(SListURL, status))
        return ServersStatus






