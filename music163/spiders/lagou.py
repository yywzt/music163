import scrapy

class LagouSpider(scrapy.Spider):
    name = "lagou"
    start_urls = [
        "https://www.lagou.com/zhaopin/Java/"
    ]

    def parse(self , response):
        for each in response.xpath("//div[@class='tip']"):
            # 职位名称
            jobMessage = each.xpath("./text()").extract_first(default="")
            print(jobMessage)
        # for each in response.xpath("//li[@class='con_list_item']"):
        #     # 职位名称
        #     jobMessage = each.xpath("./h3/text()").extract_first(default="")
        #     print(jobMessage)