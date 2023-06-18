from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.admin.widgets import AdminDateWidget

from .forms import RegisterForm
from .models import Task


def homepageView(request):
    return render(request, 'app_todo/homepage.html')


class LoginsView(LoginView):
    template_name = 'app_todo/login.html'


class LogoutsView(LogoutView):
    template_name = 'app_todo/logout.html'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_todo/register.html', {'form': form})


class TaskListView(generic.ListView):
    model = Task
    template_name = 'app_todo/todolist.html'
    context_object_name = 'tasks'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'app_todo/task.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'details', 'stop_day']
    success_url = '../'
    login_url = '/login/'

    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        form.fields['stop_day'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'details', 'stop_day']
    success_url = '../'
    login_url = '/login/'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '../'
    login_url = '/login/'
