from django.db import models
from django.contrib.auth.models import User
from task.models import Member

# Create your models here.

class WorkLog(models.Model):
    Member = models.ForeignKey(Member, on_delete=models.CASCADE),
    DateWorked = models.DateField()
    HoursWorked = models.FloatField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True)
    break_duration = models.DurationField()
    leave_type = models.CharField(max_length=50) # sick, annual, maternity, paternity, compassionate, study, unpaid
    leave_duration = models.DurationField()
    notes = models.TextField()

