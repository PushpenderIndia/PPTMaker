from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index, name="home"),
    path("waiting/<uuid:task_id>/", views.waiting, name="waiting"),
    path("check_task_progress", views.check_task_progress, name="check_task_progress")
]
