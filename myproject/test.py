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

date_selected = '2020-04-13'
check_memo = db.project_diary.find_one({'date': date_selected}, {'_id': 0})
print(check_memo)
db.project_diary.delete_one({'date': date_selected})