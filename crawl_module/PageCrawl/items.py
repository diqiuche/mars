# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OsChinaItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    icon = scrapy.Field()
    source = scrapy.Field()

class CnblogsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    icon = scrapy.Field()
    source = scrapy.Field()
