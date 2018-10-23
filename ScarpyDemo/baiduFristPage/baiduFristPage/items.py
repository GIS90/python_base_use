# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scarpy.item import Item
from scarpy.item import Field

class BaidufristpageItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class spiderItem(Item):
    title = Field()
    link = Field()
    desc = Field()
