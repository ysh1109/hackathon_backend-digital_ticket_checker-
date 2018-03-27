from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    url(r'^passengers/',views.passenger_list.as_view()),
]
