from django.urls import path
from .views import CreateTask, TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/create/', CreateTask.as_view(), name='create_task'),
]
