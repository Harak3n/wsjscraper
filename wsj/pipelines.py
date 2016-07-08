# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import datetime
from xlssettings import *
from xlutils.copy import copy
from xlrd import open_workbook

class WsjPipeline(object):

    def __init__(self):
        self.w = Workbook()
        self.ws = self.w.add_sheet('test sheet')
        self.wline = 0

        self.ws.write(self.wline, 0, 'Company', style)
        self.ws.write(self.wline, 1, 'Symbol', style)
        self.dates = 0
        self.ws.write(self.wline, 4, 'Chg', style)
        self.ws.write(self.wline, 5, '% Chg', style)
        self.ws.write(self.wline, 6, '% Float', style)
        self.ws.write(self.wline, 7, 'Days to cover', style)
        self.ws.write(self.wline, 8, 'Avg daily volume', style)

        self.xlsname = saving_directory + 'WsjData-' + \
            str(datetime.datetime.now().isoformat()).split('.')[0]+'.xls'

        self.w.save(self.xlsname)

    def process_item(self, item, spider):

        if self.dates == 0:
            self.ws.write(0, 2, item['dates'][:7], style)
            self.ws.write(0, 3, item['dates'][7:], style)
            self.dates = 1

        self.wline += 1

        styleChg = style
        stylePChg = style
        self.ws.write(self.wline, 0, item['company'], style)
        self.ws.write(self.wline, 1, item['symbol'], style)
        self.ws.write(self.wline, 2, item['date1'], style)
        self.ws.write(self.wline, 3, item['date2'], style)
        self.ws.write(self.wline, 6, item['pr_float'], style)
        self.ws.write(self.wline, 7, item['days_to_cover'], style)
        self.ws.write(self.wline, 8, item['avg_daily_volume'], style)
        if item['chg'] != '...':
            styleChg = styleRed if int(item['chg'].
                replace(',','')) < 0 else styleGreen
        self.ws.write(self.wline, 4, item['chg'], styleChg)
        if item['pr_chg'] != '...':
            stylePChg = styleRed if int(item['pr_chg'].
                replace(',','').replace('.','')) < 0 else styleGreen
        self.ws.write(self.wline, 5, item['pr_chg'], stylePChg)

        return item

    def close_spider(self, spider):
        self.w.save(self.xlsname)
