from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

import requests
from bs4 import BeautifulSoup

# # MongoDB에 insert 하기
#
# # 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

# # MongoDB에서 데이터 모두 보기
# all_users = list(db.users.find())
#
#
# # db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })
#
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# user = db.users.find_one({'name':'bobby'})
# print (user)



# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
rank = 1
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        title = a_tag.text
        star = movie.select_one('td.point').text

        doc = {
            'rank': rank,
            'title': title,
            'star': star
        }
        db.movies.insert_one(doc)
        rank += 1