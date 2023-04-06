from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('getResponse/<str:user_message>', views.getResponse, name="getResponse"),
]
