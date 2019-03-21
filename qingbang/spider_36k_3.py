# -*- coding: utf-8 -*-
import scrapy
import json
class GongSpider(scrapy.Spider):
    name = 'gong'
    # allowed_domains = ['n']
    # start_urls = ['http://n/']


    def start_requests(self):
        url = 'https://36kr.com/api//search/entity-search?page=1&per_page=40&keyword=%E5%B7%A5%E5%95%86%E8%B4%A2%E7%A8%8E&entity_type=post&sort=date&_=1552976796945'
        yield scrapy.Request(url,callback=self.parse)


    def parse(self, response):
        js = json.loads(response.text)["data"]["items"]
        for j in js:
            id = j["id"]
            yield scrapy.Request(url='https://36kr.com/p/'+str(id)+'.html',callback=self.parse_yi)


    def parse_yi(self, response):
        wen = response.css("script::text").re('props={(.*?)</p >"')
        print(wen)