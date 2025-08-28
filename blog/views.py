from django.shortcuts import render
from .models import Blog

def allBlogs(request):
    Blogs = Blog.objects.order_by('-published_date')[:5]
    return render(request, 'blog/allBlogs.html', {'blogs': Blogs})