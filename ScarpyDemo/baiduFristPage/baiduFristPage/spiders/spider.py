# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector


class SpiderSpider(Spider):
    name = "spider"
    allowed_domains = ["www.baidu.com"]
    start_urls = (
        'http://www.www.baidu.com/',
    )

    def parse(self, response):
        fileName = response.url.split("/")[-2] + '.html'
        open(fileName,'wb').write(response)
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        for site in sites:
            title = site.select('a/text()').extract()
            link = site.select('a/@href').extract()
            desc = site.select('text()').extract()
            print title, link, desc
