from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'doctor/dashboard.html')

def article(request):
    return render(request,'doctor/article.html')
