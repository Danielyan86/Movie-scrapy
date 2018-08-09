from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from ..items import MtimeMovieItem, ImageItem


class MtimeSpider(BaseSpider):
    name = "mtime"
    allowed_domains = ["movie.mtime.com/"]

    start_urls = [
        # "http://movie.mtime.com/movie/search/section/",
        "http://movie.mtime.com/31889/"
    ]

    # 定义需要爬取页面的起始和结束id
    for num in range(50000, 50006):
        start_urls.append("http://movie.mtime.com/{0}/".format(num))

    def parse(self, response):
        movie_item = MtimeMovieItem()
        movie_title = response.xpath('//title/text()').extract()[0]
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
    ]

    # 定义需要爬取页面的起始和结束id
    for num in range(31889, 32889):
        start_urls.append("http://movie.mtime.com/{0}/".format(num))

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        imgs = hxs.select('//img/@src').extract()
        item = ImageItem()
        item['image_urls'] = imgs
        return item
