from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Question


class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'  # поменял переменную контекста (пока даст все объекты)
    template_name = 'questions/list_of_questions.html'  # поменял имя шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список вопросов'   # Дополнительная переменная
        return context


class QuestionDetail(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'questions/one_question.html'  # поменял имя шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # переменная со списоком категорий
        context['categories'] = context['question'].category.all().values_list('name', flat=True)
        return context





