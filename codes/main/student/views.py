from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def activity(request):
  return render(request, 'student/activity.html')

def calendar(request):
    return render(request, 'student/calendar.html')

def profile(request):
    return render(request, 'student/profile.html')

def signup(request):
    return render(request, 'student/signup.html')

def staff(request):
    return render(request, 'student/staff.html')

def permit(request):
    return render(request, 'student/student permit .html')

def support(request):
    return render(request, 'student/suppot.html')

def tasks(request):
    return render(request, 'student/tasks.html')

def home(request):
    return render(request,'student/index.html')

def logoutUser(request):
    logout(request)
    return redirect('signup')

def login_view(request):
    if request.method == 'POST':
        # Get username and password from the request data (POST)
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Authentication successful
            login(request, user)
            return redirect('dashboard')  # Redirect to your success page
        else:
            # Authentication failed
            error_message = 'Invalid username or password.'  # Example error message
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # GET request, render the login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})