# -*- coding: utf-8 -*-

__author__ = 'tsnav-yangyn'

import urllib
from hashlib import md5

#短信报警模块，需要传进接收信息的电话号码和发送的信息
def SendMsg(tel, msg):
    assert tel
    assert msg
    phone = str(tel)
    type='100'
    sign='838181818276828a83203818a7f832013201388'
    key='f8287897f83818a7f83201320138810gb7d09657887gnff20'

    source="<submit_data><mobile>" + phone + "</mobile><type>"
    source+= type + "</type></submit_data><sign>" + sign + "</sign>" + key
    m = md5()
    m.update(source)
    md5sum = m.hexdigest()
    url = "http://122.228.183.133:8890/AService.asmx/sendSMSThird?mobile="
    url += phone + "&type=100&msg=" + msg + "&sign=" + md5sum
    urllib.urlopen(url)


if __name__=='__main__':
    SendMsg(18810650391, '杨')