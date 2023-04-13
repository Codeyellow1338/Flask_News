from flask import Flask, render_template
import requests
import random
from datetime import datetime

app = Flask(__name__)



@app.route('/')
def index():
   return render_template('index.html', 
                          title = 'Новостной сайт!', 
                          text = 'Скоро тут будут новости!')
@app.route('/news')
def news():
   return """<!DOCTYPE html>
   <html>
     <head>
        <meta charset="utf-8">
       <title>Новости</title>
     </head>
     <body>
       <h1>Новости</h1>
     </body>
   </html>"""
@app.route('/news_detail/<int:id>')
def news_detail(id):
   news = [{'title': 'Удивительное событие в школе',
         'text': 'Вчера в местной школе произошло удивительное событие - все '
                 'ученики одновременно зевнули на уроке математики. '
                 'Преподаватель был так поражен этим коллективным зевком, '
                 'что решил отменить контрольную работу.'},
        {'title': 'Случай в зоопарке',
         'text': 'В зоопарке города произошел необычный случай - ленивец '
                 'решил не лениться и взобрался на самое высокое дерево в '
                 'своем вольере. Посетители зоопарка были поражены такой '
                 'активностью и начали снимать ленивца на видео. В итоге он '
                 'получил свой собственный канал на YouTube, где он размещает '
                 'свои приключения.'},
        {'title': 'Самый красивый пёс',
         'text': 'Сегодня в парке прошел необычный конкурс - "Самый красивый '
                 'пёс". Участники конкурса были так красивы, что судьи не '
                 'могли выбрать победителя. В итоге, конкурс был объявлен '
                 'ничейным, а участники получили награды за участие, '
                 'в том числе - пакетики конфет и игрушки в виде косточек. '
                 'Конкурс вызвал большой интерес у посетителей парка, '
                 'и его решили повторить в более масштабном формате.'}]
   context = news[id]
   return render_template('news_detail.html', **context)
@app.route('/category/<string:name>')
def category_detail(name):
   return f"""
   <!DOCTYPE html>
   <html>
     <head>
       <title>Категория {name}</title>
     </head>
     <body>
     <h1>Категория {name} <h1>
     </body>
   </html>
   """

   primes = []
   number = 2
   while len(primes) < n:
       for i in range(2, number):
           if number % i == 0:
               break
       else:
           primes.append(number)
       number += 1
   return ' '.join([str(i) for i in primes])


if __name__ == '__main__':
    app.run(debug=True)