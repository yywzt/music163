# -*- coding: utf-8 -*-
import scrapy
import time

# 爬取 https://music.163.com/#/discover/playlist/ 全部歌单

class MusicDiscoverSpider(scrapy.Spider):
    name = "musicdiscover"
    start_urls = [
        # 'https://music.163.com/#/discover/playlist/'
        'http://quotes.toscrape.com/'
    ]


    def parse(self, response):
        for quote in response.css("li > a"):
            text = quote.css("::text").extract_first()
            print(text)
            # yield {
            #     'text': quote.css("p.dec > a::attr(title)").extract_first(),
            #     'author': quote.css("p.s-fc3::text").extract_first(),
            #     'href': quote.css("p.dec > a::attr(href)").extract()
            # }

        # time.sleep(5)
        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))