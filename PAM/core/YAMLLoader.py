# -*- coding: utf-8 -*-

# 处理配置文件相关的操作和类, 根据配置的是客户端模式还是服务器模式来实例化不同的配置文件类，
# 进而驱动整个系统运行

# 备注 所有的时间相关的单位都是秒

import yaml
import os
from collections import namedtuple
from Log import *

_parentFolder = getDirectory()

sendTo = namedtuple('sendTo', 'ip port')
SNMP = namedtuple('SNMP', 'enable comm version port')
database = namedtuple('database', 'enable dbtype port user password default')

yamlDir = os.path.abspath(os.path.join(os.curdir, "config"))


def loadMasterYaml(f="master.yaml"):
    yf = os.path.abspath(os.path.join(yamlDir, f))
    print yf
    assert os.path.exists(yf)
    print yf
    with open(yf) as stream:
        yunMaster = None
        step = None
        area = None
        try:
            result = yaml.load(stream.read())
            for attr in result:
                value = result[attr]
                attr = attr.lower()
                if 'step' == attr:
                    step = int(value)
                elif 'area' == attr:
                    area = value
                elif 'yunmaster' == attr:
                    ip = value.get('ip', None)
                    port = value.get('port', None)
                    assert ip is not None
                    assert port is not None
                    ip = str(ip)
                    port = int(port)
                    yunMaster = sendTo(ip, port)
            return yunMaster, step, area
        except Exception, e:
            error = "loadFromYaml got exception, error is " + str(e)
            Log.error(error)


def loadDevYaml(f="default_dev.yaml"):
    cf = {}
    ip = None
    ostype = None
    checkItem = {}
    yf = os.path.abspath(os.path.join(yamlDir, f))
    assert os.path.exists(yf)
    with open(yf) as conf:
        try:
            result = yaml.load(conf.read())
            for attr in result:
                value = result[attr]
                attr = attr.lower()
                if 'ip'== attr:
                    ip = value
                elif 'ostype' == attr:
                    ostype = value
                elif 'snmp' == attr:
                    snmpenable = value.get('enable', 1)
                    comm = value.get('community', None)
                    version = value.get('version', 1)
                    snmpport = value.get('port', None)
                    assert comm is not None
                    assert snmpport is not None
                    snmp = SNMP(int(snmpenable), comm, version, int(snmpport))
                    cf['snmp'] = snmp
                elif 'database' == attr:
                    dbEnable = value.get('enable', 0)
                    dbType = value.get('type', None)
                    dbPort = value.get('port', None)
                    dbUser = value.get('user', None)
                    dbPassword = value.get('password' , None)
                    dbDefault = value.get('default', None)
                    assert dbPort is not None
                    assert dbPassword is not None
                    db = database(int(dbEnable), dbType, int(dbPort), dbUser, str(dbPassword), dbDefault)
                    cf['db'] = db
                elif 'checkitems' == attr:
                    for item in value:
                        for i in item:
                            checkItem[i] = item[i]
            return ip, ostype, cf, checkItem
        except Exception, e:
            error = "loadDevYaml got exception, error is " + str(e)
            raise Exception(error)


if __name__ == '__main__':
    send, step, area = loadMasterYaml()
    devIp , devOsType, devCf, devCheckItem = loadDevYaml()
    print send, step, area
    print devIp, devOsType, devCf, '\n', devCheckItem