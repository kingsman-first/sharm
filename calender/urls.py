"""Defines URL patterns for calendar"""

from django.urls import path
from . import views

app_name = 'calender'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]