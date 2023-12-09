from django.urls import path

from customers.views import QuestionCreateView

urlpatterns = [
    path('api/v1/question/create/', QuestionCreateView.as_view(), name='question-create'),
]
