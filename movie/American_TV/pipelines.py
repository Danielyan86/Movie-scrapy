# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re
import urllib


class TVPipeline(object):
    def __init__(self):
        client = MongoClient()
        self.tv_doc_collection = client.TV_DB.TV_download_links
        self.tv_links = client.TV_DB.TV_pages_doc
        try:
            self.tv_doc_collection.find_one()
        except Exception as error:
            print "***Debug***{0}".format(error)
            raise AssertionError("DB initialize failed")

    def process_item(self, item, spider):
        # print "this is pipeline===============", item['down_load_link']
        if 'page_link' in item:
            pattern_link = re.compile(r'(http://www\.dygang\.com/yx/\d+/\d+.htm)')
            pattern_name = re.compile(r'>(.*)<')
            pattern_img = re.compile(r'alt="(.*])')

            for page_link in item['page_link']:
                m1 = pattern_link.search(page_link)
                m2 = pattern_name.search(page_link)
                if m1:
                    link = m1.groups()[0]
                    name = m2.groups()[0]
                    if 'img' in name:  # filter the name from another format ><img src="http://tu2.66vod.net/tupian/2014/02808.jpg" alt="\u9965\u997f\u7684\u9752\u6625[\u7b2c\u4e09\u5b6308]" width="120" height="150" border="0"></a>'
                        m3 = pattern_img.search(name)
                        if m3:
                            name = m3.groups()[0]
                    if self.tv_links.find_one({'link': link}) is None:
                        print self.tv_links.insert_one({'link': link, 'name': name})
                    else:
                        print "Page link: {0} is existing".format(link)

        elif 'download_links' in item:
            for link in item['download_links']:
                # print urllib.unquote(link + '\n\n')
                if isinstance(link, unicode):
                    link = urllib.unquote(link.encode('utf-8'))
                else:
                    print "This link:{0} is not unicode".format(link)
                result = self.tv_doc_collection.find_one({"url": link})
                if result:
                    print result
                    print "This item {0} is existing in DB, jump it".format(link)
                else:
                    if "ed2k:" in link or "ftp:" in link:
                        self.tv_doc_collection.insert_one({"url": link})
                    else:
                        print "***debug*** There is not 'ed2k' or 'ftp' found:{0}".format(link)
        else:
            print "There is no valid data"


if __name__ == '__main__':
    test_ojb = TVPipeline()
