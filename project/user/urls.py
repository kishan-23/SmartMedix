from django.contrib import admin
from django.urls import path,include
from user import views

urlpatterns = [
    path('<str:names>/',views.index,name="user-index"),
]
