from pymongo import MongoClient
from datetime import *
from random import *
import json

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)

# setting_memo = json.loads(open('credential.json').read())
# setting_str = 'mongodb://' + setting_memo['id'] + ':' + setting_memo['pwd'] + '@' + setting_memo['ip']
# client = MongoClient(setting_str, 27017)

db = client.dbsparta

emotion_keyword_pool = ['happy', 'sad', 'tired', 'depressed', 'pleasant']
keyword_pool = ['coding', 'election', 'friday']
#
def insert_one_day(emotion_index=None, emotion_keyword=None, keyword=None, year='2020', month='04', day='01', one_sentence='random', comment='random'):
    date = year+'-'+month+'-'+day
    year_month = year+'-'+month
    emotion_index = randint(1, 10)
    emotion_keyword = choice(emotion_keyword_pool)
    keyword = choice(keyword_pool)
    insert_memo = {'date': date, 'comment': comment, 'day': day,
                   'emotion_index': emotion_index, 'emotion_keyword': emotion_keyword,
                   'keyword': keyword, 'one_sentence': one_sentence, 'year_month': year_month}
    return insert_memo
#
#
# for i in ('01', '03', '05', '07', '09'):
#     # print(insert_one_day())
#     db.project_diary.insert_one(insert_one_day(year='2020', month='04', day=i))

for i in range(11, 30, 2):
    print(i)
#
#
# for i in list(db.project_diary.find({'year_month': '2020-04'}, {'_id':0, 'date':1, 'emotion_index':1 }).sort("date")):
#     print(i)

# start_date = '2020-04-01'
# end_date = '2020-04-30'
# graph_data = list(db.project_diary.find({"date": {"$gte": start_date, "$lt": end_date}},
#                                         {"_id": 0, "date": 1, "emotion_index": 1}).sort("date"))
#
# for i in graph_data:
#     print(i)
