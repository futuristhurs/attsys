from django.shortcuts import render, redirect
from .forms import ActivityLogForm

# Create your views here.

def activity_log(request):
    if request.method == 'POST':
        form = ActivityLogForm(request.POST)
        if form.is_valid():
            activity_log = form.save(commit=False)
            activity_log.student = request.user.studentprofile
            activity_log.save()
            return redirect('home')
    else:
        form = ActivityLogForm()
    return render(request, '', {'form': form})

from django.shortcuts import render
from logs.models import Attendance
from schedule.models import Calendar, Event

def calendar_view(request):
    calendar = Calendar.objects.get(name="Student Attendance")
    events = Event.objects.filter(calendar=calendar)
    return render(request, 'logs/calendar.html', {'events': events})

