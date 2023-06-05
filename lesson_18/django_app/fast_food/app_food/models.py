from django.db import models

class Pesron(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
# Create your models here.
