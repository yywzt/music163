import scrapy

class LagouSpider(scrapy.Spider):
    name = "lagou"
    start_urls = [
        "https://www.lagou.com/zhaopin/Java/"
    ]

    def parse(self , response):
        for item in response.css('.con_list_item h3'):
            jobMessage = item.css('::text').extract()
            print(jobMessage)