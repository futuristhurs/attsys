from django.urls import path
from .views import work_log

urlpatterns = [
    path('', work_log, name='work_log'),
]