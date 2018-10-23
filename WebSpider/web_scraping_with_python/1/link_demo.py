# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import re
import urlparse

from scrapy import download

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/5"


def link_crawler(seed_url, link_regex):
    assert isinstance(seed_url, basestring)
    assert isinstance(link_regex, basestring)

    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


def get_links(html):
    regex = re.compile('<a[^>]+herf=["\'](.*?)["\']', re.IGNORECASE)
    return regex.findall(html)
