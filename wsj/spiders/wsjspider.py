# -*- coding: utf-8 -*-

from itertools import islice
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from wsj.items import WsjItem

class WsjSpider(CrawlSpider):

    name = "wsjspider"
    allowed_domains = ["www.wsj.com"]
    start_urls = ['http://www.wsj.com/mdc/public/page/2_3062-shtnyse_I-listing.html']
    rules = [
        Rule(LinkExtractor(allow='/mdc/public/page/2_3062-sht\w+?_.*'),
            callback='paser',
            follow=True)
    ]

    def paser(self, response):

        result = filter(lambda x: x if x != u'\n' else 0,
                response.xpath('//table[1]/tr/td//text()').extract())

        item = WsjItem()
        item['dates'] = result[2] + result[3]

        result = result[11:]

        for i in range(len(result)/9):
            tmplist = list(islice(result,i*9,(i+1)*9))
            # item = WsjItem()
            item['company'] = tmplist[0]
            item['symbol'] = tmplist[1]
            item['date1'] = tmplist[2]
            item['date2'] = tmplist[3]
            item['chg'] = tmplist[4]
            item['pr_chg'] = tmplist[5]
            item['pr_float'] = tmplist[6]
            item['days_to_cover'] = tmplist[7]
            item['avg_daily_volume'] = tmplist[8]

            yield item
