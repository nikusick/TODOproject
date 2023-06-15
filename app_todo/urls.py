from django.urls import path

from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view()),
    path('add_task/', TaskCreateView.as_view()),
    path('task/<int:pk>/', TaskUpdateView.as_view()),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view()),
]
