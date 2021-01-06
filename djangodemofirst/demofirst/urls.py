from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'demofirst'
urlpatterns = [
    path('<int:question_id>', views.detail, name='detail'),
    path('results/<int:question_id>', views.results, name='results'),
    path('vote/<int:question_id>', views.vote, name='vote'),
    path('hello/', views.hello, name='hello'),
    path('', views.index, name='index'),

]
