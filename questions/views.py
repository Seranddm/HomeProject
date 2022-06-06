from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Answer, Comment, Category
from .forms import CreateQuestionForm, CreateAnswerForm, CreateCommentForm, UserRegisterForm, UserLoginForm
from django.views.generic.detail import SingleObjectMixin

from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.http import Http404

class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'  # поменял переменную контекста (пока даст все объекты)
    template_name = 'questions/list_of_questions.html'  # поменял имя шаблона

    def get_queryset(self):
        # Показываю только опубликованные вопросы
        return Question.objects.filter(is_published=True)

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
        context['categories'] = self.get_object().category.all()
        return context

@method_decorator(permission_required('questions.can_create_question'), name='dispatch')
class AddQuestion(CreateView):
   form_class = CreateQuestionForm
   template_name = 'questions/create_question.html'

   def get_form_kwargs(self):
       kwargs = super(AddQuestion, self).get_form_kwargs()
       kwargs['user'] = self.request.user
       return kwargs


# def AddQuestion(request):
#     if request.method == 'POST':
#         form = CreateQuestionForm(request.POST)
#         if form.is_valid():
#             question = Question.objects.create()
#             question.category.set(form.cleaned_data['category'])
#             question.text_of_question = form.cleaned_data['text_of_question']
#             question.is_published = form.cleaned_data['is_published']
#             # связываю автора с вопросом
#             question.author = request.user
#             question.save()
#             # переадресую на вопрос
#             return redirect(question)
#     else:
#         form = CreateQuestionForm()
#     return render(request, 'questions/create_question.html', {'form': form})

@method_decorator(permission_required('questions.can_create_answer'), name='dispatch')
class AddAnswer(CreateView):
   form_class = CreateAnswerForm
   template_name = 'questions/create_answer.html'

   def get_form_kwargs(self):
       kwargs = super(AddAnswer, self).get_form_kwargs()
       kwargs['user'] = self.request.user
       kwargs['id_question'] = self.kwargs['pk']
       return kwargs

   def get_success_url(self, **kwargs):
       return reverse_lazy('questionDetail', args=[self.object.question.pk])


# def AddAnswer(request, pk):
#     if request.method == 'POST':
#         form = CreateAnswerForm(request.POST)
#         if form.is_valid():
#             answer = Answer.objects.create(**form.cleaned_data)
#             answer.author = request.user
#             answer.save()
#             # связываю вопрос с ответом
#             question = Question.objects.get(pk=pk)
#             question.answer = answer
#             question.save()
#             # переадресую на вопрос
#             return redirect(question)
#     else:
#         form = CreateAnswerForm()
#     return render(request, 'questions/create_answer.html', {'form': form})

@method_decorator(permission_required('questions.can_create_comment'), name='dispatch')
class AddComment(CreateView):
   form_class = CreateCommentForm
   template_name = 'questions/create_comment.html'

   def get_form_kwargs(self):
       kwargs = super(AddComment, self).get_form_kwargs()
       kwargs['user'] = self.request.user
       kwargs['id_question'] = self.kwargs['pk']
       return kwargs

   def get_success_url(self, **kwargs):
       return reverse_lazy('questionDetail', args=[self.object.question.pk])


# def AddComment(request, pk):
#     if request.method == 'POST':
#         form = CreateCommentForm(request.POST)
#         if form.is_valid():
#             # связываю вопрос с комментом
#             question = Question.objects.get(pk=pk)
#             form.cleaned_data['question'] = question
#             comment = Comment.objects.create(**form.cleaned_data)
#             comment.author = request.user
#             comment.save()
#             # переадресую на вопрос
#             return redirect(question)
#     else:
#         form = CreateCommentForm()
#     return render(request, 'questions/create_comment.html', {'form': form})


class UpdateQuestion(UpdateView):
    model = Question
    fields = ['category', 'text_of_question']
    template_name = 'questions/update_question.html'

    @method_decorator(permission_required('questions.can_update_question'))
    def dispatch(self, request, *args, **kwargs):
        if request.user == self.get_object().author or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404



class UpdateAnswer(UpdateView):
    model = Answer
    fields = ['text_of_answer']
    template_name = 'questions/update_answer.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('questionDetail', args=[self.get_object().question.pk])

    @method_decorator(permission_required('questions.can_update_answer'))
    def dispatch(self, request, *args, **kwargs):
        if request.user == self.get_object().author or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404



class UpdateComment(UpdateView):
    model = Comment
    fields = ['text_of_comment']
    template_name = 'questions/update_comment.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('questionDetail', args=[self.get_object().question.pk])

    @method_decorator(permission_required('questions.can_update_comment'))
    def dispatch(self, request, *args, **kwargs):
        if request.user == self.get_object().author or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404


@method_decorator(permission_required('questions.can_delete_question'), name='dispatch')
class DeleteQuestion(DeleteView):
    model = Question
    template_name = 'questions/delete_question.html'
    success_url = reverse_lazy('questionList')


@method_decorator(permission_required('questions.can_delete_answer'), name='dispatch')
class DeleteAnswer(DeleteView):
    model = Answer
    template_name = 'questions/delete_answer.html'
    success_url = reverse_lazy('questionList')

    def get_success_url(self, **kwargs):
        return reverse_lazy('questionDetail', args=[self.get_object().question.pk])


@method_decorator(permission_required('questions.can_delete_comment'), name='dispatch')
class DeleteComment(DeleteView):
    model = Comment
    template_name = 'questions/delete_comment.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('questionDetail', args=[self.get_object().question.pk])


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'questions/one_category.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Каждый зарегистрированный пользователь - Обычный
            # Остальные регистрируются через админку
            user.groups.add(Group.objects.get(name='Обычный пользователь'))
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'questions/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('questionList')

    else:
        form = UserLoginForm()
    return render(request, 'questions/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('questionList')

@method_decorator(login_required, name='dispatch')
class PersonalArea(ListView):
    model = Question
    context_object_name = 'questions'  # поменял переменную контекста (пока даст все объекты)
    template_name = 'questions/personal_area.html'  # поменял имя шаблона

    def get_queryset(self):
        # Показываю вопросы конкретного пользователя
        if self.request.user.groups.filter(name='Обычный пользователь').exists():
            return Question.objects.filter(author=self.request.user)
        elif self.request.user.groups.filter(name='Администратор').exists():
            return Question.objects.filter(author=self.request.user)
        elif self.request.user.groups.filter(name='Тех. поддержка').exists():
            return Question.objects.filter(answer__author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Обычный пользователь').exists():
            context['header_query_set'] = 'Все ваши вопросы:'
            context['if_not_query_set'] = 'Вы пока не задали ни одного вопроса'
        elif self.request.user.groups.filter(name='Администратор').exists():
            context['header_query_set'] = 'Все ваши вопросы:'
            context['if_not_query_set'] = 'Вы пока не задали ни одного вопроса'
        elif self.request.user.groups.filter(name='Тех. поддержка').exists():
            context['header_query_set'] = 'Все ваши ответы:'
            context['if_not_query_set'] = 'Вы пока не ответили ни на один вопрос'
        return context


@permission_required('questions.can_create_question')
def publish_question(request, pk):
    # для опубликования вопроса из черновиков
    question = Question.objects.get(pk=pk)
    if question.author != request.user:
        raise Http404
    question.is_published = True
    question.save()
    return redirect('personal-area')

@permission_required('questions.can_create_question')
def delete_draft(request, pk):
    # для удаления вопроса из черновиков
    question_draft = Question.objects.get(pk=pk)
    if question_draft.author != request.user:
        raise Http404
    question_draft.delete()
    return redirect('personal-area')

