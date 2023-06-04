import os

from dotenv import load_dotenv
from flask import Flask, request
from sqlalchemy import (create_engine, Integer, String, Column, Text, ForeignKey)
from sqlalchemy.orm import Session, DeclarativeBase

load_dotenv()

class Base(DeclarativeBase):
    pass

password=os.getenv("PASSWORD")
engine = create_engine(f'postgresql+psycopg2://dm:{password}@localhost/blog_system_sqlalchemy')
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
    return f"""<div align="center">
                <h2>"Количество статей -->"{count_of_articles}</h2></br> 
                <button><h2><a href='/article'>Написать новую статью --></a></h2></button>
              </div>"""


@app.route('/article', methods=['GET', 'POST'])
def article_page():
    if request.method == 'GET':
        return '<form action="/article" method="POST">' \
                   '<div class="container" align="center">\
                        <textarea name="article-header" placeholder="Введите заголовок" ' \
               'cols="80" rows="3"></textarea></br>\
                        <textarea name="article-content" placeholder="Напишите здесь статью" ' \
               'cols="80" rows="20"></textarea></br>\
                        <button type="submit"><h4>Create!</h4></button>' \
                   '</div>\
                </form><h4><a href="/">Go back home</a></h4>'

    elif request.method == 'POST':
        # with Session(autoflush=False, bind=engine) as session:
        session = Session(bind=engine)
        header = request.form.get('article-header')
        article_text = request.form.get('article-content')
        art = Article(header=header, content=article_text)
        session.add(art)
        session.commit()
        return """ <div align="center">
                     <h1>text added successfully!</h1> 
                   </div>
                   <h4><a href='/article'><=Go back</a></h4>"""

if __name__ == "__main__":
    app.run()
