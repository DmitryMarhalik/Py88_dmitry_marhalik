from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=30, unique=True)


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    header = models.CharField(max_length=20, null=False, unique=True)
    content = models.TextField(max_length=300, null=False)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=20, null=False, unique=True)
    message = models.TextField(max_length=300, null=False)
    rating = models.IntegerField()
