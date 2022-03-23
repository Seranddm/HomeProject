import django.contrib.auth.models
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    info = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category)
    answer = models.OneToOneField('Answer', on_delete = models.CASCADE)
    text_of_question = models.TextField()

    def __str__(self):
        return self.text_of_question


class Comment(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    text_of_comment = models.TextField()

    def __str__(self):
        return self.text_of_comment

class Answer(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete = models.CASCADE)
    text_of_answer = models.TextField()

    def __str__(self):
        return self.text_of_answer
