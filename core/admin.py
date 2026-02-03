from django.contrib import admin
from .models import Task, Progress, Attempt

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "slug", "is_available")
    list_editable = ("is_available",)
    ordering = ("order",)

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "task", "completed", "last_score", "updated_at")
    list_filter = ("completed",)

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "task", "score", "created_at")
    list_filter = ("task",)
