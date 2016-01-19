from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

class Bla(models.Model):
    name = models.CharField(max_length=625)

class Purup(models.Model):
title = models.CharField(max_length=200)
text = models.TextField()


class Lolo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)