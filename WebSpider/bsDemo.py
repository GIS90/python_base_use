# coding:utf-8



import urllib2

from bs4 import BeautifulSoup

response = urllib2.urlopen('http://python.org/')
htmlContent = response.read()
soup = BeautifulSoup(htmlContent, 'html5lib')
print soup.title
print soup.a
print soup.a.name

print soup.a.attrs
print soup.a['title']
print soup.a.string
print soup.a.contents

print '----------------------------------------'
for child in soup.body.children:
    print child
