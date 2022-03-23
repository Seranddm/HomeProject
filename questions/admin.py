from django.contrib import admin
from .models import Question, Category, Comment, Answer
# Register your models here.

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Answer)
