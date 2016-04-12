# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider

from ..items import MtimeMovieItem, ImageItem
from pymongo import MongoClient
from scrapy.selector import HtmlXPathSelector



class MtimeSpider(BaseSpider):
    name = "mtime"
    allowed_domains = ["movie.mtime.com/"]


    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://movie.mtime.com/31889/"
        # "http://www.tubemogul.com",
    ]

    for num in range(42000, 52000):

        start_urls.append("http://movie.mtime.com/{0}/".format(num))

    def parse(self, response):
        movie_item = MtimeMovieItem()
        movie_title = response.xpath('//title/text()').extract()[0].encode('utf-8')
        if "你要访问的页面不存在" not in movie_title:
            movie_item['movie_name'] = movie_title
            movie_item['mtime_url'] = response.url
            return movie_item



class MtimePhotoSpider(BaseSpider):
    name = "mPicture"
    allowed_domains = ["movie.mtime.com/"]

    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://movie.mtime.com/31889/"
        # "http://www.tubemogul.com",
    ]

    for num in range(31889, 42000):
        start_urls.append("http://movie.mtime.com/{0}/".format(num))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        imgs = hxs.select('//img/@src').extract()
        item = ImageItem()
        item['image_urls'] = imgs
        return item

