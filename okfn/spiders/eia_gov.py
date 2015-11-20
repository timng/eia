import scrapy
from scrapy import log
from scrapy.http import Request, FormRequest
from scrapy.contrib.spiders import CrawlSpider
from okfn.items import *
from datetime import datetime

from scrapy.conf import settings
import urllib
import csv
from datetime import datetime, timedelta

class EiaSpider(CrawlSpider):
    name = "eia_daily"
    allowed_domains = ["eia.gov"]

    export_file = 'Henry_Hub_Natural_Gas_Spot_Price_Daily_%s.csv' % datetime.now().strftime('%Y-%m-%d')
    csv_header = ['Date', 'Price'] 
    writer_header = True

    start_urls = ['http://www.eia.gov/dnav/ng/hist/rngwhhdD.htm']

    def __init__(self):
        settings.set('RETRY_HTTP_CODES', [500, 503, 504, 400, 408, 404] )
        settings.set('RETRY_TIMES', 5 )
        settings.set('REDIRECT_ENABLED', True)
        settings.set('METAREFRESH_ENABLED', True)
        settings.set('USER_AGENT', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36')
   
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_price)
            # break

    def parse_price(self, response):
        for tr in response.xpath('//table[@summary="Henry Hub Natural Gas Spot Price (Dollars per Million Btu)"]//tr')[1:]:
            dateRange = ' '.join( tr.xpath('.//td[@class="B6"]/text()').extract() ).strip()
            if ' to ' in dateRange:
                dateRange = dateRange.split(' to ', 1)[0].strip()
                # 1997 Jan- 6
                date = datetime.strptime(dateRange, '%Y %b-%d').date()

                for td in tr.xpath('./td[@class="B3"]'):
                    price = ' '. join( td.xpath('./text()').extract() ).strip()

                    item = GasPriceItem()
                    
                    item['Date'] = date.strftime('%Y %b-%d')
                    item['Price'] = price.strip()

                    date = date + timedelta(days=1)
                    yield item
            

