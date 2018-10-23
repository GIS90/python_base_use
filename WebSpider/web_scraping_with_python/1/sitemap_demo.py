# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import re
from scrapy import download


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/5"


def crawl_sitemap(url):

    sitemap = download(url)
    links = re.findall('<loc>(.*?)<loc>', sitemap)
    for link in links:
        html = download(link)



url = 'http://example.webscraping.com/'
crawl_sitemap(url)



