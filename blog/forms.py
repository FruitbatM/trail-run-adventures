from django import forms
from .models import Comment, BlogPost


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('slug', 'published_date', 'author')
