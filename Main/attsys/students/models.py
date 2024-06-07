from django.db import models
from accounts.models import User

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    place_of_work = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

class LeaveRequest(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    reason = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=255, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.reason