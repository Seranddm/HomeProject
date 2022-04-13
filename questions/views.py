from django.shortcuts import render

from django.views.generic import ListView
from .models import Question


class QurestionList(ListView):
    model = Question
    context_object_name = 'questions'  # поменял переменную контекста (пока даст все объекты)
    template_name = 'questions/list_of_questions.html'  # поменял имя шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список вопросов'   # Дополнительная переменная
        return context


