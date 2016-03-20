# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from ..items import USTVItem
from pymongo import MongoClient
import urllib

client = MongoClient()  # initialize mongo client
db = client.movie_db  # access movie db


class MtimeSpider(BaseSpider):
    name = "dianyinggang"
    allowed_domains = ["dygang.com/"]
    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://www.dygang.com/yx/20151012/33190.htm"  # The walking dead
    ]

    def parse(self, response):
        movie_item = USTVItem()
        a_tag_content = response.xpath('//a/@href').extract()
        for item in a_tag_content:
            download_link = item.encode('UTF-8')
            if "The.Walking.Dead" in download_link:
                with open("TV.txt", 'a+') as f:
                    f.write("下载链接:" + urllib.unquote(download_link + '\n\n'))
                    # print "==============", a_tag_content
