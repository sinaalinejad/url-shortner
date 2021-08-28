from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from . import views
urlpatterns = [
    path("askshortened/", views.get_short_url),
    path( '<str:temp>/',views.view_func_main),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$' , views.view_func2),
    # re_path(r'^comments/(?P<outer>page-(?P<page_number>\d+))?/([0-9]+)$', views.comments) , 
]