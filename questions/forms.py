from django import forms
from .models import Question, Answer, Comment

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

