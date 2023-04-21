from django.contrib import admin
from django.urls import path, include
from  . import views

# /app/base

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('hello/',views.hello), 
    path('app/', include("base.urls")) # if app/ == app/ forward -> base/urls.py
]
