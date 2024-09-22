from django.urls import path
from .views import index, question_1, question_2, all_customers, question_3, question_4, question_5, rate_limiter_view, question_6

urlpatterns = [
    path('', index, name="index"),
    path('question_1/', question_1, name="question_1"),
    path('question_2/', question_2, name='question_2'),
    path('all_customers/', all_customers, name='all_customers'),
    path('question_3/', question_3, name='question_3'),
    path('question_4/', question_4, name='question_4'),
    path('question_5/', question_5, name="question_5"),
    path('question_6/', question_6, name='question_6'),
]

