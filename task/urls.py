from django.urls import path
from .views import createTask


urlpatterns = [
    path('', createTask, name='create_task'),
]