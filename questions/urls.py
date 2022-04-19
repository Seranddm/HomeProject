from django.urls import path, re_path
from .views import QuestionList, QuestionDetail


urlpatterns = [
    path('', QuestionList.as_view(), name='questionList'),
    re_path(r'^(?P<pk>\d+)$', QuestionDetail.as_view(), name='questionDetail'),

]