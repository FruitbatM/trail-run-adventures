from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'about',
    )


admin.site.register(Team, TeamAdmin)