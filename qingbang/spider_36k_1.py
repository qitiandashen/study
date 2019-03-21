# -*- coding: utf-8 -*-

import json

import re
import scrapy
import time

class ke36Spider(scrapy.Spider):

    name = 'ke36'

    allowed_domains = ['www.36kr.com']

    start_urls = ['https://36kr.com/']

    def parse(self, response):
        print('start parse -------------------------  ')
        word = '机器人'
        t = time.time()
        page = '1'
        print('t',t)
        for page in range(1,200):
            burl = 'http://36kr.com/api//search/entity-search?page={}&per_page=40&keyword={}&entity_type=post'.format(page,word)
            yield scrapy.Request(burl,callback=self.parse_list,dont_filter=True)

    def parse_list(self,response):
        res = response.body.decode('utf-8')
        # print(res)

        jdata = json.loads(res)
        code = jdata['code']
        timestamp = jdata['timestamp']
        timestamp_rt = jdata['timestamp_rt']
        items = jdata['data']['items']
        m_id =  items[0]['id']
        for item in items:
            m_id = item['id']
            b_url = 'http://36kr.com/p/{}.html'.format(str(m_id))
            # b_url = 'http://36kr.com/p/5137751.html'
            yield scrapy.Request(b_url,callback=self.parse_detail,dont_filter=True)

    def parse_detail(self,response):
        res = response.body.decode('utf-8')
        content = re.findall(r'<script>var props=(.*?)</script>',res)
        temstr = content[0]

        minfo = re.findall('\"detailArticle\|post\"\:(.*?)"hotPostsOf30',temstr)[0]
        print('minfo -----------------------------  ')
        minfo = minfo.rstrip(',')
        jdata = json.loads(minfo)
        print('j'*40)

        published_at = jdata['published_at']
        username = jdata['user']['name']
        title = jdata['user']['title']
        extraction_tags = jdata['extraction_tags']
        content = jdata['content']
        print(published_at,username,title,extraction_tags)
        print('*'*50)
        print(content)
