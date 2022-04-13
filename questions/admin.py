from django.contrib import admin
from .models import Question, Category, Comment, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text_of_question', 'author', )
    list_display_links = ('text_of_question', )
    search_fields = ('text_of_question', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'info')
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text_of_comment', 'author', 'question')
    search_fields = ('text_of_comment',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text_of_answer', 'author')
    search_fields = ('text_of_answer',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Answer, AnswerAdmin)
