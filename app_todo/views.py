from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.admin.widgets import AdminDateWidget

from .forms import RegisterForm
from .models import Task


def homepage(request):
    if request.user.is_authenticated:
        return redirect('/tasks')
    return redirect('/login')


class LoginsView(LoginView):
    template_name = 'app_todo/login.html'


class LogoutsView(LogoutView):
    success_url_allowed_hosts = '/'


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


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name']
    template_name = 'app_todo/todolist.html'
    success_url = '../'
    login_url = '/login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['task_list'] = Task.objects.filter(user=self.request.user.id)
        return super(TaskCreateView, self).get_context_data(**kwargs)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name']
    template_name = 'app_todo/update_task.html'
    context_object_name = 'task'
    success_url = '/'
    login_url = '/login'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'
    login_url = '/login'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
