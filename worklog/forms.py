from django import forms
from .models import WorkLog

class WorkLogForm(forms.ModelForm):
    class Meta:
        model = WorkLog
        fields = '__all__'