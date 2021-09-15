from django.shortcuts import render, get_object_or_404

from .models import BlogPost


def blog(request):
    """
    A view to return the Blog page
    """

    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/basecampblog.html', context)


def blog_post(request, slug):
    """
    Add blog post to the blog
    """

    blog = get_object_or_404(BlogPost, slug=slug)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_post.html', context)
