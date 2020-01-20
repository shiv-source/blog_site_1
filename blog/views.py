from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def home(request):
    blog_post = BlogPost.objects.all()
    return render(request,'home.html',{'blog_post': blog_post })