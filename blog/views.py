from django.shortcuts import render
from .models import Blog

# Create your views here.
def Blog_Page(request):
    blogs = Blog.objects
    return render(request, 'blog.html', {'blogs':blogs})