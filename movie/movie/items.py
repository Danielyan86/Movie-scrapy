# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class MtimeMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = Field()
    mtime_urls = Field()
    image = Field()


class ImageItem(scrapy.Item):
    image_urls = Field()
    images = Field()
    image_paths = Field()
