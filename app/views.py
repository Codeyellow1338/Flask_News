from flask import render_template, redirect, url_for

from . import app, db
from .forms import NewsForm
from .models import Category, News

@app.route('/')
def index():
    news_list = News.query.all()
    return render_template('index.html',
                           news=news_list)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news_detail = News.query.get(id)
    return render_template('news_detail.html',
                           news=news_detail)


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('news_detail', id=news.id))
    return render_template('add_news.html',
                           form=form)