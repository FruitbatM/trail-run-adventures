from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import CommentForm, BlogForm


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


@login_required
def add_blog(request):
    """ Add a post to the blog """

    if not request.user.is_superuser:
        messages.error(request, 'Only TRΛIL RUN ΛDVENTURES Team has permission\
                                to add a Blog post.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            # Create Blog object but don't save to database yet
            new_blog = blog_form.save(commit=False)
            # Assign the auther to the new blog and save it
            new_blog.author = request.user
            new_blog.save()
            messages.success(request, 'Successfully added a blog post!')
        else:
            messages.error(request, 'Failed to add the blog post. \
                           Please ensure the form is valid.')
    else:
        blog_form = BlogForm()

    context = {
        'blog_form': blog_form,
    }

    return render(request, 'blog/add_blog.html', context)
