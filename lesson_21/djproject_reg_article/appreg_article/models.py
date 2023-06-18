from django.db import models
from django.contrib.auth.models import User
# class Author(models.Model):
#     # name = models.ForeignKey(auth_users, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=20, unique=True,null=True)
#     email = models.EmailField(max_length=30, unique=True, null=True)

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    header = models.CharField(max_length=20, null=False, unique=True)
    content = models.TextField(max_length=300, null=False)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=20, null=False, unique=True)
    message = models.TextField(max_length=300, null=False)
    rating = models.IntegerField()
from django.db import models

# Create your models here.
