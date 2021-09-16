from django.shortcuts import render
from blog.models import BlogPost


def index(request):
    """
    A view to return the index page
    """

    blog_home = BlogPost.objects.all().order_by('pk')[:2]

    context = {
        'blog_home': blog_home
    }

    return render(request, 'home/index.html', context)
