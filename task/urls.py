from django.urls import path
from . import views

#app_name = 'task'

urlpatterns = [
    path('', views.taskList, name='task_list'),  # Add this line to add the view function to our URL pattern
    path('create/', views.createTask, name='create_task'),
    path('<int:pk>/', views.taskDetails, name='task_details'),
    path('<int:pk>/update/', views.taskUpdate, name='task_update'),
    path('<int:pk>/delete/', views.taskDelete, name='task_delete'),
]