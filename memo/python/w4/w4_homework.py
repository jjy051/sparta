from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('w4_homework.html')



@app.route('/orders', methods=['GET'])
def read_reviews():
    all_orders = list(db.orders.find({}, {'_id':0}))
    return jsonify({'result':'success', 'orders': all_orders})

@app.route('/orders', methods=['POST'])
def write_reviews():
    name_receive = request.form['name']
    quantity_receive = request.form['quantity']
    address_receive = request.form['address']
    phone_number_receive = request.form['phone_number']

    order = {
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'phone_number': phone_number_receive
    }
    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 접수되었습니다'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)