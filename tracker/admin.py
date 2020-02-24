from django.contrib import admin

from .models import Tasks

@admin.register(Tasks)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'task_type', 'created_at', 'updated_at', 'user', 'in_progress')
