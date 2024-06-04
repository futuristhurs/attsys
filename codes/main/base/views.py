from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# from .models import Room, Topic, Topic, Message
# from .forms import RoomForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Check for stored user type (e.g., from session) and redirect accordingly
            if request.session.get('user_type') == 'student':
                return redirect('student:login')
            elif request.session.get('user_type') == 'staff':
                return redirect('staff:login')
            else:
                # Handle invalid user type
                return render(request, 'base/login.html', {'error_message': 'Invalid user type'})
        else:
            # Handle invalid credentials
            return render(request, 'base/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')



    return render(request, 'base/register.html', {'form': form})






