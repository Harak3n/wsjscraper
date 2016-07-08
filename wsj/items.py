# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WsjItem(scrapy.Item):
    company = scrapy.Field()
    symbol = scrapy.Field()
    date1 = scrapy.Field()
    date2 = scrapy.Field()
    chg = scrapy.Field()
    pr_chg = scrapy.Field()
    pr_float = scrapy.Field()
    days_to_cover = scrapy.Field()
    avg_daily_volume = scrapy.Field()