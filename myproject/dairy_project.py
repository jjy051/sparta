from pymongo import MongoClient
from datetime import *
from flask import Flask, render_template, jsonify, request
import json
app = Flask(__name__)

client = MongoClient('localhost', 27017)

# setting_memo = json.loads(open('credential.json').read())
# setting_str = 'mongodb://' + setting_memo['id'] + ':' + setting_memo['pwd'] + '@' + setting_memo['ip']
# client = MongoClient(setting_str, 27017)

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


@app.route('/api/calendar/popup', methods=['POST'])
def calendar_popup_load():
    popup_diary_date = request.form['diary_date']
    popup_diary = db.project_diary.find_one({'date': popup_diary_date}, {'_id':0})

    return jsonify({'result': 'success', 'popup_diary':popup_diary})

@app.route('/api/lifegraph', methods=['POST'])
def render_graph_data():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    expression_mode = request.form['expression_mode']

    graph_data = list(db.project_diary.find({"date": {"$gte": start_date, "$lt": end_date}},
                                            {"_id":0, "date":1, "emotion_index":1, "keyword":1, "emotion_keyword":1}).sort("date"))
    date_list = []
    emotion_index_list = []
    emotion_keyword_list = []
    keyword_list = []
    for i in graph_data:
        # date_list.append(datetime.strptime(i['date'], '%Y-%m-%d').date())
        date_list.append(i['date'])
        emotion_index_list.append(i['emotion_index'])
        emotion_keyword_list.append(i['emotion_keyword'].split(','))
        keyword_list.append(i['keyword'].split(','))
    #
    # start_date_format = datetime.strptime(start_date, '%Y-%m-%d')
    # end_date_format = datetime.strptime(end_date, '%Y-%m-%d')
    # days_num = (end_date_format - start_date_format).days
    # for i in range(days_num+1):
    #     target_date = (start_date_format+timedelta(i)).strftime('%Y-%m-%d')
    #     if target_date == graph_data[0]['date']:
    #         temp_value = graph_data.pop(0)
    #         date_list.append(temp_value['date'])
    #         emotion_index_list.append(temp_value['emotion_index'])
    #     else:
    #         date_list.append(target_date)
    #         emotion_index_list.append(0)

    return jsonify({'result': 'success',
                    'date_list': date_list,
                    'emotion_index_list': emotion_index_list,
                    'emotion_keyword_list': emotion_keyword_list,
                    'keyword_list': keyword_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)