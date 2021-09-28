from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import BlogPost, Comment
from .forms import CommentForm


def blog(request):
    """ A view to return the Blog page """

    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/basecampblog.html', context)


def blog_post(request, slug):
    """ A view to add blog post to the blog """

    blog = get_object_or_404(BlogPost, slug=slug)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog_post
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, 'Comment was successfully posted.')
    else:
        comment_form = CommentForm()

    context = {
        'blog': blog,
        'blog_post': blog_post,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_post.html', context)
