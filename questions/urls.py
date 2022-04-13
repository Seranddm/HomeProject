from django.urls import path
from .views import QurestionList

urlpatterns = [
    path('', QurestionList.as_view(), name='questionList')
]