# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from pymongo import MongoClient

client = MongoClient()

db = client.movie_db


class DmozSpider(BaseSpider):
    name = "mtime"
    allowed_domains = ["movie.mtime.com/"]
    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://movie.mtime.com/31889/"
    ]
    for num in range(40000, 60000):
        start_urls.append("http://movie.mtime.com/{0}/".format(num))

    def parse(self, response):
        movie_title = response.xpath('//title/text()').extract()[0].encode('utf-8')
        if "你要访问的页面不存在" not in movie_title:
            table_test = db.movie_doc
            table_test.insert_one({'movie_name': movie_title}).inserted_id
