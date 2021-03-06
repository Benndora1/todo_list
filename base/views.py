from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


from . models import Task


class TaskList(ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'

class CreateTask(CreateView):
    model = Task
    template_name = 'base/create_task.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')

class UpdateTask(UpdateView):
    model = Task
    template_name = 'base/update_task.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')