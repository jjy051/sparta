from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movies = db.movies
score =movies.find_one({'title': '어벤져스: 엔드게임'})['star']
print(score)

for movie in movies.find({'star': score}):
    print(movie['title'])

score = 9.38
movies.update_many({'star':score}, {'$set':{'star':0}})

for movies in movies.find({'star': 0}):
    print(movie['title'])
