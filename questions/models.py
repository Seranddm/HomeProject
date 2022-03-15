from django.db import models



class User(models.Model):
    pseudonym = models.CharField(max_length=40, primary_key=True)
    POSITIONS = (
        ('user', 'Пользователь'),
        ('developer', 'Разработчик'),
    )
    position = models.CharField(max_length=15, choices=POSITIONS)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    info = models.TextField()


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    author
    category
    answer
    text_of_question = models.TextField()


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    author
    question
    text_of_comment = models.TextField()

class Answer(models.Model):
    author
    question
    text_of_answer = models.TextField()
