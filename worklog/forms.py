from django import forms
from .models import workLog

class WorkLogForm(forms.ModelForm):
    class Meta:
        model = workLog
        fields = '__all__'