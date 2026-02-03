from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/<slug:slug>/", views.task_detail, name="task_detail"),
    path("api/complete/<slug:slug>/", views.api_complete_task, name="api_complete_task"),
]
