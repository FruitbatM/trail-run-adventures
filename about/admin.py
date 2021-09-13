from django.contrib import admin
from .models import Instructor


class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'about_content_1',
    )


admin.site.register(Instructor, InstructorAdmin)
