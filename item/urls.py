"""This separeted url file. Has been created to render the detail.html by using the pk of the item  as path"""
from django.urls import path

from . import views

app_name= 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]