# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class DmozSpider(BaseSpider):
    name = "mtime"
    allowed_domains = ["movie.mtime.com/"]
    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://movie.mtime.com/31889/"
    ]
    for num in range(40000, 6000):
        start_urls.append("http://movie.mtime.com/{0}/".format(num))

    def parse(self, response):
        with open("movie.txt", 'a+') as f:
            movie_title = response.xpath('//title/text()').extract()[0].encode('utf-8')
            if "你要访问的页面不存在" not in movie_title:
                f.write(movie_title)
                f.write('\n')
