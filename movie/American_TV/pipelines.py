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
        self.tv_doc_collection = client.TV_DB.TV_doc
        try:
            self.tv_doc_collection.find_one()
        except Exception as error:
            print "***Debug***{0}".format(error)
            raise AssertionError("DB initialize failed")

    def process_item(self, item, spider):
        # print "this is pipeline===============", item['down_load_link']
        for link in item['download_links']:
            print urllib.unquote(link + '\n\n')
            pattern = re.compile(r'(The.Walking.Dead.S\d+E\d+)')
            m = pattern.search(link)
            if m:
                name = m.groups()[0]
                result = self.tv_doc_collection.find_one({"name": name})
                if result:
                    print "This item {0} is existing in DB, jump it".format(result)
                else:

                    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                    self.tv_doc_collection.insert_one({"url": link, 'name': name, 'record_time': current_time})
            else:
                print "***debug*** There is no TV name found"


if __name__ == '__main__':
    test_ojb = TVPipeline()
