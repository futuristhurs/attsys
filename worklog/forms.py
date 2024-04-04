from django import forms
from .models import WorkLog

class WorkLogForm(forms.ModelForm):
    class Meta:
        model = WorkLog
        fields = '__all__'
        
class WorkLogForm(forms.ModelForm):
    planned_hours = forms.ChoiceField(choices=[], label="Planned Hours")  # Dynamic choices
    leave_duration = forms.ChoiceField(choices=[], label="Leave Duration (Optional)")  # Dynamic choices

    class Meta:
        model = WorkLog
        fields = ('planned_hours', 'leave_duration', 'break_duration', 'leave_type', 'notes')
