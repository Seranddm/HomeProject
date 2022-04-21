import django.contrib.auth.models
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    info = models.TextField(verbose_name='Информация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'   # Имя модели в единственном числе
        verbose_name_plural = 'Категории'   # Имя модели во множественном числе


class Question(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, default='User', on_delete = models.SET_DEFAULT, verbose_name='Автор')
    category = models.ManyToManyField(Category, related_name='questions', verbose_name='Категория')
    answer = models.OneToOneField('Answer', null=True , blank=True ,on_delete = models.SET_NULL)
    text_of_question = models.TextField(verbose_name='Текст вопроса')

    def __str__(self):
        return self.text_of_question

    class Meta:
        verbose_name = 'Вопрос'   # Имя модели в единственном числе
        verbose_name_plural = 'Вопросы'   # Имя модели во множественном числе
        unique_together = ('author', 'text_of_question')

    def get_absolute_url(self):
        return reverse('questionDetail', args=[str(self.id)])

    def comment_exist(self):
        """ Проверка наличия комментов """
        return self.comments.exists()


class Comment(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, default='User', on_delete = models.SET_DEFAULT,
                               verbose_name='Автор')
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='comments', verbose_name='Вопрос')
    text_of_comment = models.TextField(verbose_name='Текст комментария')

    def __str__(self):
        return self.text_of_comment

    class Meta:
        verbose_name = 'Комментарий'   # Имя модели в единственном числе
        verbose_name_plural = 'Комментарии'   # Имя модели во множественном числе

class Answer(models.Model):
    author = models.ForeignKey(django.contrib.auth.models.User, default='User', on_delete = models.SET_DEFAULT,
                               verbose_name='Автор')
    text_of_answer = models.TextField(verbose_name='Текст ответа')

    def __str__(self):
        return self.text_of_answer

    class Meta:
        verbose_name = 'Ответ'   # Имя модели в единственном числе
        verbose_name_plural = 'Ответы'   # Имя модели во множественном числе
