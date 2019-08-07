from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_post, name='feed'),
    path('new/', views.create_post, name='create_post')
]