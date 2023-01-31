from django.contrib import admin
from django.urls import path
from .views import employee_list

urlpatterns = [
    path('emps/', employee_list)
]