from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
    
class School(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField( max_length=100, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    participants = models.ManyToManyField(User, blank=True, related_name='students')
    roles = models.ManyToManyField(Role, blank=True, related_name='roles')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.completed and not self.completed_date:  
            self.completed_date = timezone.now()  
        super().save(*args, **kwargs) 

class Member(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school', null=True)
    user = models.OneToOneField(User, related_name='user', on_delete=models.SET_NULL, null=True)
    skills = models.TextField(blank=True)
    matric_id = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.user.username

class Subtask(models.Model):
    task = models.ForeignKey(Task, related_name='task', on_delete=models.CASCADE)
    title = models.CharField( max_length= 200)
    discription = models.TextField()
    member = models.ForeignKey(User, related_name='member', on_delete=models.CASCADE, null=True)

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Task, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:20]