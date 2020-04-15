from pymongo import MongoClient
from datetime import *

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# db.project_diary.remove();
# date_memo = db.project_diary.find_one({'date': '2020-04-11'}, {'_id': 0})
# print(date_memo)
# print(date_memo['emotion_keyword'])

# doc = {'name': 'ttt', 'img': 'ttt'}
# db.project_diary.insert_one(doc)

# date_memo = db.project_diary.find_one({'date': '2020-04-11'}, {'_id': 0, 'date': 0})
#
#
# a = "http://localhost:5000/api/memo?date=2020-04-12"
# b = a.split('?date=')[1]
# print(b)

year_month = '2020-04'
print(year_month)
print(type(year_month))
month_diary = list(db.project_diary.find({'year_month': year_month}, {'_id': 0}).sort("date"))

print(type(month_diary[0]))
print(month_diary[0])

for i in month_diary:
    print(i)
# day_list = list(db.project_diary.find({'year_month': year_month}, {'date':1}).sort({'date':1}))
