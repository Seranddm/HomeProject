from django import forms
from .models import Question, Answer, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CreateQuestionForm(forms.ModelForm):
    is_published = forms.BooleanField(label='Опубликовать вопрос? Если нет, то он будет сохранен в черновиках.',
                                      required=False)
    class Meta:
        model = Question
        fields = ['category', 'text_of_question', 'is_published']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CreateQuestionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        question = super(CreateQuestionForm, self).save(commit=False)
        # связываю автора с вопросом
        question.author = self.user
        if commit:
            question.save()
        return question


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text_of_answer']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.id_question = kwargs.pop('id_question')
        super(CreateAnswerForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        answer = super(CreateAnswerForm, self).save(commit=False)
        # связываю автора с ответом
        answer.author = self.user
        # связываю вопрос с ответом
        question = Question.objects.get(pk=self.id_question)
        question.answer = answer
        if commit:
            answer.save()
            question.save()
        return answer


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_of_comment']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.id_question = kwargs.pop('id_question')
        super(CreateCommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super(CreateCommentForm, self).save(commit=False)
        # связываю автора с комментом
        comment.author = self.user
        # связываю коммент с вопросом
        question = Question.objects.get(pk=self.id_question)
        comment.question = question
        if commit:
            comment.save()
        return comment


class UserRegisterForm(UserCreationForm):
    # Форма регистрации нового пользователя
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    # Форма аутентификации
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
