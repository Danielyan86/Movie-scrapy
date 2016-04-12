# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

from ..items import ImageItem


class MtimePhotoSpider(BaseSpider):
    name = "topit"
    allowed_domains = ["www.topit.me/"]

    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        # "http://www.topit.me",  # http://www.topit.me/tag/美女
        "http://www.topit.me/broad?type=search&k=风景",
        "http://www.topit.me/broad?type=search&k=风景&t=1&p=2"]

    # for i in range(3, 11):
    #     start_urls.append("http://www.topit.me/broad?type=search&k=%E7%BE%8E%E5%A5%B3&t=1&p={0}".format(i))

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={"is_click": "1"}, callback=self.parse)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        imgs = hxs.select('//img/@data-original').extract()
        item = ImageItem()
        item['image_urls'] = imgs
        return item
