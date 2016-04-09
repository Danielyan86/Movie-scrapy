# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re
import logging
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)


class MoviePipeline(object):
    year_pattern = re.compile(r'\((\d+)\)')
    name_pattern = re.compile(r'(.*)\(')

    def __init__(self):
        client = MongoClient()
        # db = client.movie_db
        self.movie_doc_collection = client.movie_db.movie_doc

    def process_item(self, item, spider):

        if not self.movie_doc_collection.find({'mtime_url': item['mtime_url']}).count():
            logger.info("insert the moive into db")

            m = self.year_pattern.search(item['movie_name'])
            year = m.groups()[0] if m else None
            m = self.name_pattern.search(item['movie_name'])
            name = m.groups()[0] if m else item['movie_name']
            result = self.movie_doc_collection.insert_one(
                {"moive": name, 'year': year, 'mtime_url': item['mtime_url']})
            logger.info(result.inserted_id)
        else:
            print "movie:{0} is existing in db, jump it".format(item['mtime_url'])
        return item


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
