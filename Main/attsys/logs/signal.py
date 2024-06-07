from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Attendance
from schedule.models import Event, Calendar

@receiver(post_save, sender=Attendance)
def create_attendance_event(sender, instance, created, **kwargs):
    if created:
        Event.objects.create(
            title=f"{instance.student.user.username} - {instance.status}",
            start=instance.date,
            end=instance.date,
            calendar=Calendar.objects.get(name="Student Attendance")
        )
