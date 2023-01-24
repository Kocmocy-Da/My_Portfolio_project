from django.shortcuts import render, get_object_or_404
from .models import Post


def all_blogs(request):
    posts = Post.objects.order_by('-time') # [:5] - последние 5 постов, сортировка по дате
    return render(request, 'blog/all_blogs.html', {'posts': posts})


def detail(request, blogid):
    blog = get_object_or_404(Post, pk=blogid)
    return render(request, 'blog/detail.html', {'blog': blog})
