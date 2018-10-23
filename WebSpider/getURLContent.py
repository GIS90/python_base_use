# -*- coding: utf-8 -*-

import urllib2
import re
url = 'http://localhost:6080/arcgis/rest/services/?f=sitemap'
request = urllib2.Request(url)
request.add_header('User-agent', 'Mozilla 5.10')
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')
print content
reg = '<loc>(.*?)</loc>'
pattern = re.compile(reg, re.S)
result = re.findall(pattern,content)
print result
