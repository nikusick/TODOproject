from django.urls import path

from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, LoginsView, \
    LogoutsView, register_view

urlpatterns = [
    path('', TaskListView.as_view()),
    path('add_task/', TaskCreateView.as_view()),
    path('task/<int:pk>', TaskDetailView.as_view()),
    path('task/<int:pk>/update/', TaskUpdateView.as_view()),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view()),
    path('login/', LoginsView.as_view()),
    path('logout/', LogoutsView.as_view()),
    path('register/', register_view),

]
