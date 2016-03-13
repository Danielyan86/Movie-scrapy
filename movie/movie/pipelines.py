# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re

client = MongoClient()
db = client.movie_db
movie_doc_collection = client.movie_db.movie_doc

year_pattern = re.compile(r'\((\d+)\)')
name_pattern = re.compile(r'(.*)\(')


class MoviePipeline(object):
    def process_item(self, item, spider):

        if not movie_doc_collection.find({'mtime_url': item['mtime_url']}).count():
            print("insert the moive into db")
            m = year_pattern.search(item['movie_name'])
            if m:

                year = m.groups()[0]
            m = name_pattern.search(item['movie_name'])
            if m:
                name = m.groups()[0]
                result = movie_doc_collection.insert_one({"moive": name, 'year': year, 'mtime_url': item['mtime_url']})
                print(result.inserted_id)
        else:
            print("movie is existing in db, jump it")
