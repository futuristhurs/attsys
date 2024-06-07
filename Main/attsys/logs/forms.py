from django import forms
from .models import ActivityLog

class ActivityLogForm(forms.ModelForm):
    class Meta:
        model = ActivityLog
        fields = ['date', 'activity']