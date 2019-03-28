from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def Blog_Page(request):
    blogs = Blog.objects
    return render(request, 'blog.html', {'blogs':blogs})

def Blog_Text(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    #   blogs = Blog.objects   , {'blogs': blogs}
    return render(request, 'Blog_Text.html', {'blog': blog})

