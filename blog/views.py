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
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post_id = post_id
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, 'Comment was successfully added!')
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_post.html', context)
