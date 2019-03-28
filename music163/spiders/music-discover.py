# -*- coding: utf-8 -*-
import json

from scrapy import Spider, Request, FormRequest
from ..settings import DEFAULT_REQUEST_HEADERS

# 爬取 https://music.163.com/#/discover/playlist/ 全部歌单

class MusicDiscoverSpider(Spider):
    name = "musicdiscover"
    allowed_domains = ["163.com"]
    base_url = 'https://music.163.com'
    # ids = ['1001','1002','1003','2001','2002','2003','6001','6002','6003','7001','7002','7003','4001','4002','4003']
    ids = ['1001']
    # initials = [i for i in range(65, 91)]+[0]
    initials = [65]
    # start_urls = [
    #     'https://music.163.com/#/discover/playlist/'
    # ]

    def start_requests(self):
        for id in self.ids:
            for initial in self.initials:
                url = '{url}/discover/artist/cat?id={id}&initial={initial}'.format(url=self.base_url,id=id,initial=initial)
                yield Request(url, callback=self.parse_index)

    # 获得所有歌手的url
    def parse_index(self, response):
        # print(response.text)
        for sel in response.xpath('//ul[@id="m-artist-box"]//li'):
            artist=sel.re('href\=\"\/artist\?id\=[(0-9)]{4,9}')
            for artistid in artist:
                # print(artistid)
                artist_url = self.base_url + '/artist?' + artistid[14:]
                yield Request(artist_url,callback= self.parse_artist_pre)

    def parse_artist_pre(self,response):
        print(response)