#coding:utf-8


import urllib2
import re
import eventlet



def fetch(url,rlt,pool):
    assert isinstance(url, basestring)
    assert isinstance(rlt, set)
    reg = '(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))'
    pattern = re.compile(reg)
    print 'fetch : %s'%url
    print pool.free()
    print pool.running()
    print pool.size
    if pool.size==500:
        pool.resize(1000)
    data = urllib2.urlopen(url).read()
    for url_match in pattern.finditer(data):
        url_new = url_match.group(0)
        if url_new not in rlt:
            rlt.add(url_new)
            pool.spawn_n(fetch, url_new,rlt,pool)


if __name__=='__main__':
    url = 'http://www.muzixing.com'
    pool = eventlet.GreenPool(size=500)
    rlt = set()
    fetch(url,rlt,pool)
    pool.waitall()
    print 'Success ....'

