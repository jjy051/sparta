from pymongo import MongoClient
from datetime import date

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def home_func():
    return render_template('index.html')

@app.route('/today.html')
def today_func():
    return render_template('today.html')

@app.route('/calendar.html')
def calendar_func():
    return render_template('calendar.html')

@app.route('/lifegraph.html')
def lifegraph_func():
    return render_template('lifegraph.html')

@app.route('/my_emotion.html')
def my_emotion_func():
    return render_template('my_emotion.html')

# API 통신 부분
@app.route('/api/memo/save', methods=['POST'])
def save_memo():
    selected_date = request.form['date']
    doc = {
        'date': selected_date,
        'year_month': selected_date.split('-')[0]+'-'+selected_date.split('-')[1],
        'day': selected_date.split('-')[2],
        'emotion_index': request.form['emotion_index'],
        'emotion_keyword': request.form['emotion_keyword'],
        'keyword': request.form['keyword'],
        'one_sentence': request.form['one_sentence'],
        'comment': request.form['comment']
    }
    db.project_diary.update_one({'date': selected_date}, {'$set': doc}, upsert=True)
    return jsonify({'result': 'success'})


@app.route('/api/memo/load', methods=['POST'])
def load_memo():
    ### GET 방식에서는 url 파싱으로 정보 획득 가능함.
    # date_selected = request.url.split('?date=')[1]
    date_selected = request.form['date']
    date_memo = db.project_diary.find_one({'date': date_selected}, {'_id': 0})

    return jsonify({'result': 'success', 'date_memo': date_memo})

@app.route('/api/memo/delete', methods=['POST'])
def delete_memo():
    date_selected = request.form['date']
    check_memo = db.project_diary.find_one({'date': date_selected}, {'_id': 0})

    db.project_diary.delete_one({'date': date_selected})
    return jsonify({'result': 'success', 'check': check_memo})


@app.route('/api/calendar/load', methods=['POST'])
def calendar_load():
    year_month = request.form['year_month']
    month_diary = list(db.project_diary.find({'year_month': year_month}, {'_id':0}).sort("date"))

    return jsonify({'result': 'success', 'month_diary': month_diary})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)