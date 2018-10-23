# coding:utf-8


import urllib
import bs4

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#
# soup=BeautifulSoup(html_doc,'html5lib')
# print soup
#
#
#
#
#
# url='http://ruixuechuntang.fang.com/house/1010710579/housedetail.htm'
#
# request=urllib2.Request(url)
# request.add_header('User-agent','Mozilla 5.10')
# response=urllib2.urlopen(request)
# content=response.read().decode('utf-8')
# buf = StringIO.StringIO(content)
#
# video_webpage = buf.read()
#
# print video_webpage




# cookie=cookielib.CookieJar()
# handle=urllib2.HTTPCookieProcessor(cookie)
# opener=urllib2.build_opener(handle)
# reponse=opener.open(url)
#
# f=urllib.urlopen(url)
# print f.read()
# print '-----------------------------'
# print f.info()
# print '-----------------------------'
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value
# print '-----------------------------'
# print f.getcode()
# print '-----------------------------'
# print f.geturl()
# f='1.html'
# filename=urllib.urlretrieve(url,f)
# print 'Save Success .'
#
# urllib.urlcleanup()
# print '11111111111111111111111111111111111111111111111111'
#
#
# import httplib
# conn1 = httplib.HTTPConnection('www.baidu.com:80')
# #conn2 = httplib.HTTPconnection('www.baidu.com',80)
# conn3 = httplib.HTTPConnection('www.baidu.com',80,True,10)
# print conn1
# #print conn2
# print conn3
#
#


import httplib

url = 'www.baidu.com'
port = 80
strict = False
timeout = 300
# connHttp=httplib.HTTPConnection(url,port,strict,timeout)
# print connHttp
url = 'localhost:6080/arcgis/rest/services/SampleWorldCities/MapServer?f=jsapi'
connHttp = httplib.HTTPConnection("url", 80, False, timeout)
values = {'User-agent': 'Mozilla 5.10'}
handler = urllib.urlencode(values)
connHttp.request('get', '/')
response = connHttp.getresponse()

print response.read()
print '---------------------------'
print response.reason
print '---------------------------'

print '---------------------------'
print response.version
print '---------------------------'
print response.status
print '---------------------------'
print response.fp
