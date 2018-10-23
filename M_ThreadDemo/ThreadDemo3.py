# -*- coding: utf-8 -*-

import time, datetime
import urllib2


def chk_qq(qqnum):
    chkurl = 'http://wpa.qq.com/pa?p=1:' + `qqnum` + ':1'
    a = urllib2.urlopen(chkurl)
    length = a.headers.get("content-length")
    a.close()
    print datetime.datetime.now()
    if length == '2329':
        return 'Online'
    elif length == '2262':
        return 'Offline'
    else:
        return 'Unknown Status!'


qq = 137935207
stat = chk_qq(qq)
print `qq` + ' is ' + stat
