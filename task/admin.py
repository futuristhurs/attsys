from django.contrib import admin
from .models import Role,Subject, Task, Member, Subtask, Chat, School
# Register your models here.

admin.site.register(Role)
admin.site.register(Subject)
admin.site.register(Task)
admin.site.register(Member)
admin.site.register(Subtask)
admin.site.register(Chat)
admin.site.register(School)