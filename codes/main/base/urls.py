from django.urls import path
from . import views

app_name ='base'

urlpatterns = [
    path('', views.login, name="Login"),
    path('logout/', views.logoutUser, name="Logout"),
    path('register/', views.registerPage, name="Register"),   
]