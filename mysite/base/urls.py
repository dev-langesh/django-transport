from django.urls import path
from  . import views

# /app/base

urlpatterns = [
    path("base/",views.base) # base/ == base/
]

