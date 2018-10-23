#- * - coding: utf-8 - * -

from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from Demo.items import Item

class DmozSpider(Spider):  
    name = "spider"  
    allowed_domains = ["dmoz.org"]  
    start_urls = [
        "http://www.dmoz.org/",
        "http://www.baidu.com/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",  
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"  
    ]  
  
    def parse(self, response):  
        filename = response.url.split("/")[-2] + '.html'
        open(filename, 'wb').write(response.body)
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            item = Item()
            item['title'] = site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['desc'] = site.select('text()').extract()
            items.append(item)
        return items
