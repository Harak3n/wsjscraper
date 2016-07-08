# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
from xlssettings import *
from xlutils.copy import copy
from xlwt import *
from xlrd import open_workbook

class WsjPipeline(object):

    def __init__(self):
        w = Workbook()
        ws = w.add_sheet('test sheet')

        ws.write(0, 0, 'Company', style)
        ws.write(0, 1, 'Symbol', style)
        ws.write(0, 2, 'date1', style)
        ws.write(0, 3, 'date2', style)
        ws.write(0, 4, 'Chg', style)
        ws.write(0, 5, '% Chg', style)
        ws.write(0, 6, '% Float', style)
        ws.write(0, 7, 'Days to cover', style)
        ws.write(0, 8, 'Avg daily volume', style)

        self.xlsname = 'WsjData-'+str(datetime.datetime.now().isoformat()).split('.')[0]+'.xls'

        w.save(self.xlsname)


    def process_item(self, item, spider):
        rb = open_workbook(self.xlsname,formatting_info=True)
        r_sheet = rb.sheet_by_index(0)
        r = r_sheet.nrows
        wb = copy(rb)
        ws = wb.get_sheet(0)

        styleChg = style
        stylePChg = style
        ws.write(r, 0, item['company'], style)
        ws.write(r, 1, item['symbol'], style)
        ws.write(r, 2, item['date1'], style)
        ws.write(r, 3, item['date2'], style)
        ws.write(r, 6, item['pr_float'], style)
        ws.write(r, 7, item['days_to_cover'], style)
        ws.write(r, 8, item['avg_daily_volume'], style)
        if item['chg'] != '...':
            styleChg = styleRed if int(item['chg'].
                replace(',','')) < 0 else styleGreen
        ws.write(r, 4, item['chg'], styleChg)
        if item['pr_chg'] != '...':
            stylePChg = styleRed if int(item['pr_chg'].
                replace(',','').replace('.','')) < 0 else styleGreen
        ws.write(r, 5, item['pr_chg'], stylePChg)

        wb.save(self.xlsname)

        return item
