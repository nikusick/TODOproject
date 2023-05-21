from django.urls import path

from .views import TaskListView, TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view()),
    path('add_task/', TaskCreateView.as_view()),
]
