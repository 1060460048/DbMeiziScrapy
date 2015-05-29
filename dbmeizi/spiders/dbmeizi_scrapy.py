from scrapy import Spider
from scrapy.selector import Selector
from dbmeizi.items import MeiziItem

class dbmeiziSpider(Spider):
    name = "dbmeiziSpider"
    allowed_domin =["dbmeinv.com"]
    strArray = []
    for i in range(2598,1,-1):
        str = "http://www.dbmeinv.com/?pager_offset=%d" % i
        strArray.append(str)
    start_urls = strArray
            
    def parse(self, response):
        divResults = Selector(response).xpath('//div[@class="img_single"]')
        for div in divResults:
            item = MeiziItem()
            href = div.xpath('.//a')[0]
            img = div.xpath('.//img')[0]
            item['topiclink'] = href.xpath('@href').extract()[0]
            item['title'] = img.xpath('@title').extract()[0] 
            item['imgsrc'] = img.xpath('@src').extract()[0]
            item['startcount'] = 0
            yield item
