# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from ..items import USTVItem
import urllib


class WalkingDeadSpider(BaseSpider):
    name = "walkingdead"
    allowed_domains = ["dygang.com/"]
    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://www.dygang.com/yx/20151012/33190.htm"  # The walking dead
    ]

    def parse(self, response):
        wd_item = USTVItem()
        a_tag_content = response.xpath('//a/@href').extract()
        # for item in a_tag_content:
        #     download_link = item.encode('UTF-8')
        #     if "The.Walking.Dead" in download_link:
        #         wd_item['down_load_links'].append(download_link)
        wd_item['download_links'] = \
            [item for item in a_tag_content if "The.Walking.Dead" in item.encode('utf-8')]
        return wd_item


class ShieldSpider(BaseSpider):
    name = "shield"
    allowed_domains = ["dygang.com/"]
    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://www.dygang.com/yx/20150930/33060.htm"  # Shield
    ]

    def parse(self, response):
        a_tag_content = response.xpath('//a/@href').extract()
        for item in a_tag_content:
            download_link = item.encode('UTF-8')
            if "dy131" in download_link:
                with open("shield.html", 'a+') as f:
                    f.write("下载链接: " + urllib.unquote(download_link + '\n\n'))
