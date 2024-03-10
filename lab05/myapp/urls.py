from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.list_people, name='list_people'),
]
