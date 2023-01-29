from django.urls import path

from .views import QuestionsList, ChoicesDetail

urlpatterns = [
    path('questions', QuestionsList.as_view()),
    path('question/<int:pk>/', ChoicesDetail.as_view()),
    ]
