# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZolSpjkItem(scrapy.Item):
    brand = scrapy.Field()
    name = scrapy.Field()
    typeBig = scrapy.Field()
    typeMedium = scrapy.Field()
    typeSmall = scrapy.Field()

