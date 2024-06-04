from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.


def staff(request):
    return render(request, 'staff/staff.html')

def tasks(request):
    return render(request, 'staff/tasks.html')

def logbook(request):
    return render(request, 'staff/logbook info.html')

def ttrryy(request):
    return render(request, 'staff/try.html')

def signup(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to your success page
            else:
                # Authentication failed, handle error (e.g., display error message)
                pass
    else:
        form = AuthenticationForm()
    return render(request, 'staff/signup.html', {'form':form})
def home(request):
    
    return render(request,'staff/index.html')


