from django.db import models
from accounts.models import User

# Create your models here.

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    ...
