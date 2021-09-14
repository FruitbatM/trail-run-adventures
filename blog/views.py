from django.shortcuts import render
from .models import BlogPost


def blog(request):
    """
    A view to return the Blog page
    """

    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)
