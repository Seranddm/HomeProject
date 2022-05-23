from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Answer, Comment, Category
from .forms import CreateQuestionForm, CreateAnswerForm, CreateCommentForm, UserRegisterForm, UserLoginForm
from django.views.generic.detail import SingleObjectMixin

from django.urls import reverse_lazy
from django.contrib.auth import login, logout


class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'  # поменял переменную контекста (пока даст все объекты)
    template_name = 'questions/list_of_questions.html'  # поменял имя шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список вопросов'  # Дополнительная переменная
        context['categories'] = Category.objects.all()
        return context


class QuestionDetail(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'questions/one_question.html'  # поменял имя шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # переменная со списоком категорий
        context['categories'] = SingleObjectMixin.get_object(self).category.all()
        return context


#class AddQuestion(CreateView):
#    form_class = CreateQuestionForm
#    template_name = 'questions/create_question.html'


def AddQuestion(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.create()
            question.category.set(form.cleaned_data['category'])
            question.text_of_question = form.cleaned_data['text_of_question']
            # связываю автора с вопросом
            question.author = request.user
            question.save()
            # переадресую на вопрос
            return redirect(question)
    else:
        form = CreateQuestionForm()
    return render(request, 'questions/create_question.html', {'form': form})



def AddAnswer(request, pk):
    if request.method == 'POST':
        form = CreateAnswerForm(request.POST)
        if form.is_valid():
            answer = Answer.objects.create(**form.cleaned_data)
            answer.author = request.user
            answer.save()
            # связываю вопрос с ответом
            question = Question.objects.get(pk=pk)
            question.answer = answer
            question.save()
            # переадресую на вопрос
            return redirect(question)
    else:
        form = CreateAnswerForm()
    return render(request, 'questions/create_answer.html', {'form': form})


def AddComment(request, pk):
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            # связываю вопрос с комментом
            question = Question.objects.get(pk=pk)
            form.cleaned_data['question'] = question
            comment = Comment.objects.create(**form.cleaned_data)
            comment.author = request.user
            comment.save()
            # переадресую на вопрос
            return redirect(question)
    else:
        form = CreateCommentForm()
    return render(request, 'questions/create_comment.html', {'form': form})


class UpdateQuestion(UpdateView):
    model = Question
    fields = ['category', 'text_of_question']
    template_name = 'questions/update_question.html'


class DeleteQuestion(DeleteView):
    model = Question
    template_name = 'questions/delete_question.html'
    success_url = reverse_lazy('questionList')


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'questions/one_category.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'questions/register.html', {'form' : form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('questionList')

    else:
        form = UserLoginForm()
    return render(request, 'questions/login.html', {'form' : form})


def user_logout(request):
    logout(request)
    return redirect('questionList')
