from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.signup, name="signup"),
    path('permit/', views.permit, name='Student-Permit'),
    path('activity/', views.activity, name='Activity'),
    path('calendar/', views.calendar, name='Calendar'),
    path('profile/', views.profile, name='Profile'),
    path('support/', views.support, name='Support'),
    path('Dashboard/', views.home, name= "home"),
    path('logout/', views.logoutUser, name="logout"),
]