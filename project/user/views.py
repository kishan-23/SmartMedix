from django.shortcuts import render
#from project import blogs.models
from blogs.models import Post
# Create your views here.
def index(request,names):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    contex={
        'uname':names,
        'bloglist':queryset
    }
    return render(request,'user/index.html',contex)
