from django.contrib import admin
from django.urls import path
from .views import employee_view

urlpatterns = [
    path('emps/', employee_view)
]