from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.signup, name="signup"),
   path('staff/', views.staff, name='Staff'),
   path('tasks/', views.tasks, name='Tasks'),
   path('logbbok/', views.logbook, name='Logbook Info'),
   path('tasks/', views.tasks, name='Tasks'),
   path('try/', views.ttrryy, name='Try'),
   path('Dashboard/', views.home, name= "home"),
   
   ]