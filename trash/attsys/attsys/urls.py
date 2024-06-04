"""
URL configuration for attsys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from staff import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activity/', views.activity, name='Activity'),
    path('calendar/', views.calendar, name='Calendar'),
    path(' ', include, name='Home Page'),
    path('logbbok/', views.logbook, name='Logbook Info'),
    path('login/', views.login, name='Login'),
    path('profile/', views.profile, name='Profile'),
    path('signup/', views.signup, name='Sign-Up'),
    path('staff/', views.staff, name='Staff'),
    path('permit/', views.permit, name='Student-Permit'),
    path('support/', views.support, name='Suppot'),
    path('tasks/', views.tasks, name='Tasks'),
    path('try/', views.ttrryy, name='Try')
]
