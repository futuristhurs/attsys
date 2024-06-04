from django.shortcuts import render

# Create your views here.

def activity(request):
  return render(request, 'frontend/activity.html')

def calendar(request):
    return render(request, 'frontend/calendar.html')

def home(request):
    return render(request, 'frontened/homepage 1.html')

def logbook(request):
    return render(request, 'frontend/logbook info.html')

def login(request):
    return render(request, 'frontend/login page.html')

def profile(request):
    return render(request, 'frontend/profile.html')

def signup(request):
    return render(request, 'frontend/signup 1.html')

def staff(request):
    return render(request, 'frontend/staff.html')

def permit(request):
    return render(request, 'frontend/student permit .html')

def support(request):
    return render(request, 'frontend/suppot.html')

def tasks(request):
    return render(request, 'frontend/tasks.html')

def ttrryy(request):
    return render(request, 'frontend/try.html')