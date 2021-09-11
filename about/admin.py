from django.contrib import admin
from .models import Instructor


class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'about',
    )


admin.site.register(Instructor, InstructorAdmin)
