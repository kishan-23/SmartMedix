from . import views
from django.urls import path

urlpatterns = [
    path('', views.listview, name='blogs-home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]