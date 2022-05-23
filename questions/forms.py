from django import forms
from .models import Question, Answer, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category', 'text_of_question']


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text_of_answer']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_of_comment']


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
