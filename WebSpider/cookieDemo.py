#coding:utf-8


import cookielib
import urllib2
filename='cookie.txt'
cookie=cookielib.MozillaCookieJar(filename)
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
url='http://www.baidu.com'
response=opener.open(url)
for item in cookie:
    print 'Name : '+item.name
    print 'Value : '+item.value
cookie.save(ignore_discard=True,ignore_expires=True)


cookie=cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
request=urllib2.Request(url)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response=opener.open(request)
print response.read()


