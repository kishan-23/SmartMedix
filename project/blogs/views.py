from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views import generic
from .models import Post

def listview(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    contex={ 'bloglist':queryset }
    #return HttpResponse("This is blog")
    return render(request,'blogs/index.html',contex)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'