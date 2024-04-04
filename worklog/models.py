from django.db import models
from django.utils import timezone
from task.models import Member


# Create your models here.

class WorkLog(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE),
    DateWorked = models.DateField(default=timezone.now().date())
    planned_hours =  models.FloatField(blank=True, null=True)
    actual_hours = models.FloatField(blank=True, null=True)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(blank=True, null=True)
    break_duration = models.DurationField(blank = True, null = True)
    leave_type = models.CharField(max_length=50, blank=True) # sick, annual, maternity, paternity, compassionate, study, unpaid
    leave_duration = models.DurationField(blank=True, null=True)  # Optional leave duration
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member} - {self.DateWorked}"

    def save(self, *args, **kwargs):
        if self.check_out:
            try:
                self.actual_hours = (self.check_out - self.check_in).total_seconds() / 3600  # Calculate in hours
            except TypeError:  # Handle cases where check_in or check_out is None
                self.actual_hours = None
        super().save(*args, **kwargs)