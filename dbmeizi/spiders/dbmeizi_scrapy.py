from scrapy import Spider
from scrapy.selector import Selector
from dbmeizi.items import MeiziItem

class dbmeiziSpider(Spider):
    name = "dbmeiziSpider"
    allowed_domin =["dbmeizi.com"]
    start_urls = [
            
        "http://www.dbmeizi.com", 
    ]

    def parse(self, response):
        liResults = Selector(response).xpath('//li[@class="span3"]')
        for li in liResults:
            for img in li.xpath('.//img'):
                item = MeiziItem()
                item['title'] = img.xpath('@data-title').extract()
                item['dataid'] = img.xpath('@data-id').extract()
                item['datasrc'] = img.xpath('@data-src').extract()
                item['startcount'] = 0
                yield item
