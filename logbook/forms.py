from django import forms

from .models import Day, Activity

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['entryDate']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['startTime', 'endTime', 'description', 'category']