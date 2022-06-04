from django.urls import path
from .views import *

urlpatterns = [
    path('', QuestionList.as_view(), name='questionList'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='questionDetail'),
    path('add_question/', AddQuestion.as_view(), name='addQuestion'),
    path('add_answer/<int:pk>/', AddAnswer.as_view(), name='addAnswer'),
    path('add_comment/<int:pk>/', AddComment.as_view(), name='addComment'),
    path('update_question/<int:pk>/', UpdateQuestion.as_view(), name='updateQuestion'),
    path('update_answer/<int:pk>/', UpdateAnswer.as_view(), name='updateAnswer'),
    path('update_comment/<int:pk>/', UpdateComment.as_view(), name='updateComment'),
    path('delete_question/<int:pk>/', DeleteQuestion.as_view(), name='deleteQuestion'),
    path('delete_answer/<int:pk>/', DeleteAnswer.as_view(), name='deleteAnswer'),
    path('delete_comment/<int:pk>/', DeleteComment.as_view(), name='deleteComment'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='categoryDetail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('personal-area/', PersonalArea.as_view(), name='personal-area'),
    path('publish_question/<int:pk>/', publish_question, name='publish_question'),
    path('delete-draft/<int:pk>/', delete_draft, name='delete_draft'),

]
