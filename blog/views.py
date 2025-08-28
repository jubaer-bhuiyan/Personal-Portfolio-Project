from django.shortcuts import render

def allBlogs(request):
    return render(request, 'blog/allBlogs.html')