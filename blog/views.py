from django.shortcuts import render, get_object_or_404
from .models import Blog

def allBlogs(request):
    Blogs = Blog.objects.order_by('-published_date')[:5]
    return render(request, 'blog/allBlogs.html', {'blogs': Blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})