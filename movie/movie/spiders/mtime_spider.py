# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from ..items import MtimeMovieItem
from pymongo import MongoClient

client = MongoClient()  # initialize mongo client
db = client.movie_db    # access movie db


class MtimeSpider(BaseSpider):
    name = "mtime"
    allowed_domains = ["movie.mtime.com/"]
    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://movie.mtime.com/31889/"
    ]
    for num in range(0, 300000):
        start_urls.append("http://movie.mtime.com/{0}/".format(num))

    def parse(self, response):
        movie_item = MtimeMovieItem()
        movie_title = response.xpath('//title/text()').extract()[0].encode('utf-8')
        if "你要访问的页面不存在" not in movie_title:
            movie_item['movie_name'] = movie_title
            movie_item['mtime_url'] = response.url
            return movie_item
