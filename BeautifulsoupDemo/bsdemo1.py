# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

# 格式化
print soup.prettify()
# tag
print 'name:', soup.p.name
print 'attr:', soup.p.attrs['class']
print 'string:', soup.p.string
# 遍历文档树

for child in soup.descendants:

    print child

print soup.find_all(True)