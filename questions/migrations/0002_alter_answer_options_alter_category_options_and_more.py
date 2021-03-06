# Generated by Django 4.0.3 on 2022-04-21 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(default='User', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text_of_answer',
            field=models.TextField(verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='category',
            name='info',
            field=models.TextField(verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default='User', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='questions.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text_of_comment',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default='User', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ManyToManyField(related_name='questions', to='questions.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text_of_question',
            field=models.TextField(verbose_name='Текст вопроса'),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('author', 'text_of_question')},
        ),
    ]
