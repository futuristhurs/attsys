from django.db import models
from students.models import StudentProfile
from schedule.models import Calendar, Event
from datetime import datetime

# Create your models here.

class ActivityLog(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField()
    activity = models.TextField()

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    ]

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)



# Create a calendar
calendar, created = Calendar.objects.get_or_create(name="Student Attendance")

# Create events based on attendance records
def create_attendance_event(attendance):
    Event.objects.create(
        title=f"{attendance.student.user.username} - {attendance.status}",
        start=attendance.date,
        end=attendance.date,
        calendar=calendar
    )

# Example: Call this function whenever you create an attendance record
attendance = Attendance.objects.create(student=student, date=datetime.now(), status='present')
create_attendance_event(attendance)
