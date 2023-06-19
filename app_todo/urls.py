from django.urls import path

from .views import TaskCreateView, TaskDeleteView, LoginsView, \
    LogoutsView, register_view, homepage

urlpatterns = [
    path('', homepage),
    path('tasks/', TaskCreateView.as_view()),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view()),
    path('login/', LoginsView.as_view()),
    path('logout/', LogoutsView.as_view()),
    path('register/', register_view),

]
