from django.urls import path
from . import views

urlpatterns = [
    path('question_one',views.question_one, name="question_one")
]
