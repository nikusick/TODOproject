from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView

from .models import Task


def homepageView(request):
    return render(request, 'app_todo/homepage.html')


class TaskListView(generic.ListView):
    model = Task
    template_name = 'app_todo/todolist.html'
    context_object_name = 'tasks'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'app_todo/task.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    fields = ['name', 'details', 'stop_day']
    success_url = '../'

