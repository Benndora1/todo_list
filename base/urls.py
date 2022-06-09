from django.urls import path
from .views import CreateTask, TaskList, TaskDetail, UpdateTask

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task_update/<int:pk>/', UpdateTask.as_view(), name='task_update'),
    path('create_task/', CreateTask.as_view(), name='create_task'),
]
