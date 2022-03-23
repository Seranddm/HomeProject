import django.contrib.auth.models
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    info = models.TextField()


class Question(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category)
    answer = models.OneToOneField('Answer')
    text_of_question = models.TextField()


class Comment(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question)
    text_of_comment = models.TextField()

class Answer(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete = models.CASCADE)
    text_of_answer = models.TextField()
