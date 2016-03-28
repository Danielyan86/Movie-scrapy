from pymongo import MongoClient


def get_all_tv_page_links_dianyinggang():
    client = MongoClient()
    tv_links_cllection = client.TV_DB.TV_pages_doc
    result = tv_links_cllection.find()
    return map(lambda x: x[u'link'], result)


if __name__ == '__main__':
    print get_all_tv_page_links_dianyinggang()
