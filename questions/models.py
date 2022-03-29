import django.contrib.auth.models
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, default='User', on_delete = models.SET_DEFAULT())
    category = models.ManyToManyField(Category, related_name='questions')
    answer = models.OneToOneField('Answer', null=True , blank=True ,on_delete = models.SET_NULL())
    text_of_question = models.TextField()

    def __str__(self):
        return self.text_of_question


class Comment(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, default='User', on_delete = models.SET_DEFAULT())
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='comments')
    text_of_comment = models.TextField()

    def __str__(self):
        return self.text_of_comment

class Answer(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, default='User', on_delete = models.SET_DEFAULT())
    text_of_answer = models.TextField()

    def __str__(self):
        return self.text_of_answer
