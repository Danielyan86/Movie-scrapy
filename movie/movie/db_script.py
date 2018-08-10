from pymongo import MongoClient
import re

client = MongoClient()
movie_doc_obj = client.movie_db.movie_doc

year_pattern = re.compile(r'(\d+)')
name_pattern = re.compile(r'(.*)\(')


def fetch_movie_year_from_name():
    for item in movie_doc_obj.find():

        m = year_pattern.search(item['year'])
        if m:
            year = int(m.groups()[0])
        else:
            print("not exist number, jump it")
            continue

        movie_doc_obj.update_one({'movie_name': item['movie']},
                                 {'$set': {'year': year,
                                           'movie_name': item['movie'].replace(m.groups()[0],
                                                                               "")}})  # update one collection with specified name

# 查询某个年代的电影
def get_movie_with_name(year):
    for item in movie_doc_obj.find():
        if item['year'] == year:
            print(item)


if __name__ == '__main__':
    get_movie_with_name("2004")
