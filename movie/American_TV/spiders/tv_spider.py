# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from ..items import USTVItem, PageItem
import urllib
from util import get_links


class TVNameSpider(BaseSpider):
    name = "dianyinggang"
    allowed_domains = ["dygang.com"]
    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://www.dygang.com/yx/"  # Shield
    ]
    for num in range(2, 107):
        start_urls.append("http://www.dygang.com/yx/index_{0}.htm".format(num))

    def parse(self, response):
        page_link = PageItem()
        a_tag = response.xpath('//a').extract()
        # a_tag_name = response.xpath('//a/text()').extract()
        page_link['page_link'] = a_tag
        return page_link

        # print type(content)
        # with open("TV_name.html", 'a+') as f:
        #     f.write(urllib.unquote(content + '\n\n'))

        # for item in a_tag_name:
        #     name = item.encode('UTF-8')
        #     with open("TV_name.html", 'a+') as f:
        #         f.write("下载链接: " + urllib.unquote(name + '\n\n'))


class WalkingDeadSpider(BaseSpider):
    name = "dyglinks"
    allowed_domains = ["dygang.com"]
    print get_links.get_all_tv_page_links_dianyinggang()
    start_urls = get_links.get_all_tv_page_links_dianyinggang()
    # start_urls = ["http://www.dygang.com/yx/20150930/33060.htm",
    #               'http://www.dygang.com/yx/20160319/34371.htm',
    #               'http://www.dygang.com/yx/20150922/32990.htm', ]

    def parse(self, response):
        tv_links = USTVItem()
        a_tag_content = response.xpath('//a/@href').extract()
        tv_links['download_links'] = [item for item in a_tag_content if item.encode('utf-8')]
        return tv_links


class ShieldSpider(BaseSpider):
    name = "shield"
    allowed_domains = ["dygang.com/"]
    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://www.dygang.com/yx/20150930/33060.htm",  # Shield
        'http://www.dygang.com/yx/20160319/34371.htm',
        'http://www.dygang.com/yx/20150922/32990.htm',

    ]

    def parse(self, response):
        a_tag_content = response.xpath('//a/@href').extract()
        for item in a_tag_content:
            download_link = item.encode('UTF-8')
            if "dy131" in download_link:
                with open("shield.html", 'a+') as f:
                    f.write("下载链接: " + urllib.unquote(download_link + '\n\n'))
