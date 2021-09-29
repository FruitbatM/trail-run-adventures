from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .models import BlogPost, Comment
from .forms import CommentForm


def blog(request):
    """ A view to return the Blog page """

    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/basecampblog.html', context)


def blog_post(request, post_id):
    """ A view to show an individual blog post and posting comments. """

    post = get_object_or_404(BlogPost, pk=post_id)
    comment_form = CommentForm

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        name = get_object_or_404(User, id=request.user.id)
        if name.is_superuser:
            name = ""
        comment_form = comment_form.save(commit=False)
        comment_form.post = post
        comment_form.name = name
        if comment_form.is_valid():
            comment_form.post = post
            comment_form.name = name
            comment_form.save()
            messages.success(request, 'Comment was successfully added!')
            return HttpResponseRedirect(reverse(
                'blog_post', args=[str(post_id)]))
        else:
            messages.error(request, 'It seems that your comment cannot \
                be posted!')
            return HttpResponseRedirect(reverse(
                'blog_post', args=[str(post_id)]))

    context = {
        'post': post,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_post.html', context)
