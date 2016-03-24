# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re
import urllib
import time


class TVPipeline(object):
    year_pattern = re.compile(r'\((\d+)\)')
    name_pattern = re.compile(r'(.*)\(')

    def __init__(self):
        client = MongoClient()
        # db = client.movie_db
        self.tv_doc_collection = client.TV_DB.TV_doc

    def process_item(self, item, spider):
        # print "this is pipeline===============", item['down_load_link']
        for link in item['download_links']:
            # print "download link{0}".format(link)
            print urllib.unquote(link + '\n\n')

            pattern = re.compile(r'(The.Walking.Dead.S\d+E\d+)')
            m = pattern.search(link)
            if m:
                print "====++", m.groups()[0]
                name = m.groups()[0]
            current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            self.tv_doc_collection.insert_one({"url": link, 'name': name, 'record_time': current_time})
            # if not self.tv_doc_collection.find({'mtime_url': item['mtime_url']}).count():
            #     print "insert data into db"
            #     result = self.movie_doc_collection.insert_one(
            #         {"moive": name, 'year': year, 'mtime_url': item['mtime_url']})
            #     print result.inserted_id
            # else:
            #     print "movie:{0} is existing in db, jump it".format(item['mtime_url'])
            # return item
