from django.contrib import admin
from .models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published_date',
        'pk',
        'slug',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_added',
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
