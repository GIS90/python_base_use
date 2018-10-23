# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/6/6'
"""

import re
import urllib
import urllib2


def translate(send):
    rlt = send.isalpha()
    if rlt:
        values = {'text': send, 'hl': 'en', 'tl': 'zh-CN'}
    else:
        values = {'text': send, 'hl': 'zh-CN', 'tl': 'en'}
    google_url = 'http://translate.google.cn/'
    # baidu_url = 'http://fanyi.baidu.com/'
    # youdao_url = 'http://fanyi.youdao.com/'
    # jinshan_url = 'http://fy.iciba.com/'
    data = urllib.urlencode(values)
    request = urllib2.Request(google_url, data)
    request.add_header('User-Agent', 'Mozilla 5.10')
    response = urllib2.urlopen(request)
    html = response.read()
    p = re.compile(r"(?<=TRANSLATED_TEXT=).*?;")
    m = p.search(html)
    rlt = m.group(0).strip(';')
    print rlt


if __name__ == '__main__':
    translate('你吃饭了吗')
    translate('eat')
