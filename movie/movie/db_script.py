from pymongo import MongoClient
import re

client = MongoClient()
movie_doc_obj = client.movie_db.movie_doc

year_pattern = re.compile(r'\((\d+)\)')
name_pattern = re.compile(r'(.*)\(')


def fetch_movie_year_from_name():
    for item in movie_doc_obj.find():

        m = year_pattern.search(item['movie'])
        if m:
            year = int(m.groups()[0])
        else:
            print("not exist number, jump it")
            continue

        movie_doc_obj.update_one({'movie_name': item['movie_name']},
                                 {'$set': {'year': year,
                                           'movie_name': item['movie_name'].replace(m.groups()[0],
                                                                                    "")}})  # update one collection with specified name


if __name__ == '__main__':
    fetch_movie_year_from_name()
