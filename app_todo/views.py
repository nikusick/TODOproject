from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.admin.widgets import AdminDateWidget

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

    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        form.fields['stop_day'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name', 'details', 'stop_day']
    success_url = '../'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '../'
