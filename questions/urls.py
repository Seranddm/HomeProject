from django.urls import path
from .views import QuestionList, QuestionDetail, AddQuestion, AddAnswer, AddComment, UpdateQuestion, DeleteQuestion


urlpatterns = [
    path('', QuestionList.as_view(), name='questionList'),
    path('<int:pk>/', QuestionDetail.as_view(), name='questionDetail'),
    path('add_question/', AddQuestion.as_view(), name='addQuestion'),
    path('add_answer/<int:pk>/', AddAnswer, name='addAnswer'),
    path('add_comment/<int:pk>/', AddComment, name='addComment'),
    path('update_question/<int:pk>/', UpdateQuestion.as_view(), name='updateQuestion'),
    path('delete_question/<int:pk>/', DeleteQuestion.as_view(), name='deleteQuestion'),
]