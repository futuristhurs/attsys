from django.urls import path
from .views import workLog

urlpatterns = [
    path('', workLog, name='work_log'),
]