from scrapy.spider import Spider
from scrapy.selector import Selector 

class TwxshSpider4WorksURL(Spider):
    name="twxshspider4worksurl"
    allowed_domains=["http://eic.jnu.edu.cn/"]
    start_urls=[
        "http://eic.jnu.edu.cn/twxsh/channels/104.html"]
    def parse(self,response):
        sel=Selector(response)
        #title=sel.xpath('body/table[2]/tr[1]/td/table/tr/td[3]/table/tr[1]/td/table/tr/td[0]/a/text()').extract()
        urls=sel.xpath('body/table[3]/tr[2]/td[1]/table[1]/tr[1]/td[3]/table[1]/tr[2]/td[1]/table/tr[1]/td[1]/a/@href')
        
        filename=response.url.split('/')[-1]
        f=open(filename,'wb')
        for url in urls:
            f.write('http://eic.jnu.edu.cn'+url.extract()+'\r\n')
        f.close

