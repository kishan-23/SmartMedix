from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
    path('doctor', views.doctor, name="doctor")

]
