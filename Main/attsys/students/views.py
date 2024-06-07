from django.shortcuts import render, redirect
from .models import StudentProfile
from .forms import LeaveRequestForm

# Create your views here.

def home(request):
    profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'students/home.html', {'profile': profile})


def request_leave(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.student = request.user.studentprofile
            leave_request.save()
            return redirect('home')
    else:
        form = LeaveRequestForm()
    return render(request, 'students/request_leave.html', {'form': form})

