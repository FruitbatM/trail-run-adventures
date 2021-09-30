from django import forms
from .models import Comment, BlogPost


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['slug'].widget.attrs['placeholder'] = 'ending of the link'
        self.fields['intro_paragraph_1'].widget.attrs[
                    'placeholder'] = '100 - 500 characters'
        self.fields['intro_paragraph_2'].widget.attrs[
                    'placeholder'] = '100 - 500 characters'
        self.fields['subheading_1'].widget.attrs[
                    'placeholder'] = 'max 80 characters'
        self.fields['blog_content_1'].widget.attrs[
                    'placeholder'] = 'min 250 characters'
        self.fields['subheading_2'].widget.attrs[
                    'placeholder'] = 'max 80 characters'
        self.fields['blog_content_2'].widget.attrs[
                    'placeholder'] = 'min 250 characters'
        self.fields['blog_content_3'].widget.attrs[
                    'placeholder'] = 'min 250 characters'
        self.fields['subheading_3'].widget.attrs[
                    'placeholder'] = 'max 80 characters'
        self.fields['blog_content_4'].widget.attrs[
                    'placeholder'] = 'min 250 characters'
        self.fields['blog_content_5'].widget.attrs[
                    'placeholder'] = 'min 250 characters'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-blog-form-field'
