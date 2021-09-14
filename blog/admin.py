from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published_date',
        'pk',
        'slug',
    )


admin.site.register(BlogPost, BlogPostAdmin)
