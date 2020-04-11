from pymongo import MongoClient
from datetime import *

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

db.project_diary.remove();

# doc = {'name': 'ttt', 'img': 'ttt'}
# db.project_diary.insert_one(doc)
