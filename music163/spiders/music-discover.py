# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver

browser = webdriver.Chrome()


# 爬取 https://music.163.com/#/discover/playlist/ 全部歌单

class MusicDiscoverSpider(scrapy.Spider):
    name = "musicdiscover"
    start_urls = [
        'https://music.163.com/#/discover/playlist/'
    ]


    def parse(self, response):
        browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[0])
        text = browser.find_elements_by_xpath("//ul[@class='m-pl-container']//li")
        print(text)
        # print("href:",response.css('iframe::attr(href)'))
        # print("id:",response.css('iframe::attr(id)'))
        # print("name:",response.css('iframe::attr(name)'))
        # for quote in response.xpath("//ul[@class='f-cb']//li"):
        # # for quote in response.xpath("//li[@class='lb'] | //li[@class='ltb']"):
        #     text = quote.xpath("./a/em/text()").extract_first()
        #     print(text)

        # time.sleep(5)
        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))