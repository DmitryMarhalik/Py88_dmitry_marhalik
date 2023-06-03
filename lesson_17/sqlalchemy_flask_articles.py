from flask import Flask, request
from sqlalchemy import (create_engine, Integer, String, Column, Text, ForeignKey)
from sqlalchemy.orm import Session, DeclarativeBase


class Base(DeclarativeBase):
    pass


engine = create_engine('postgresql+psycopg2://dm:113019@localhost/blog_system_sqlalchemy')
app = Flask(__name__)


class Author(Base):
    __tablename__ = 'author'
    id = Column('id', Integer(), primary_key=True)
    nickname = Column('nickname', String(255), unique=True)
    email = Column('email', String(255), unique=True)


class Article(Base):
    __tablename__ = 'article'
    id = Column('id', Integer(), primary_key=True,index=True)
    author_id = Column('author_id',Integer())# ForeignKey('author.id'))
    header = Column('header', String(255), unique=False)
    content = Column('content', Text(), nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column('id', Integer(), primary_key=True, index=True)
    article_id = Column('article_id', ForeignKey('article.id'), nullable=False)
    nickname = Column('nickname', String(255), unique=True)
    message = Column('message', Text(), nullable=False)
    rating = Column('rating', Integer(), nullable=False)


Base.metadata.create_all(bind=engine)


@app.route('/')
def main_page():
    session = Session(bind=engine)
    count_of_articles = session.query(Article).count()
    return f"Количество статей --> {count_of_articles}</br>" \
           f"<button><a href='/article'>Написать новую статью --></a></button>"


@app.route('/article', methods=['GET', 'POST'])
def article_page():
    if request.method == 'GET':
        return '<form action="/article" method="POST">' \
                   '<div class="container" align="center">\
                        <textarea name="article-header" placeholder="Введите заголовок" ' \
               'cols="80" rows="3"></textarea></br>\
                        <textarea name="article-content" placeholder="Здесь пишется статья" ' \
               'cols="80" rows="20"></textarea></br>\
                        <button type="submit">Create!</button>' \
                   '</div>\
                </form><h4><a href="/">Go back home</a></h4>'

    elif request.method == 'POST':
        session = Session(bind=engine)
        header = request.form.get('article_header')
        article_text = request.form.get('article-content')
        art = Article(header=header, content=article_text)
        session.add(art)
        session.commit()
        return """ <h1>text added successfully!</h1> 
                   <h4><a href='/article'><=Go back</a></h4>"""

if __name__ == "__main__":
    app.run()
