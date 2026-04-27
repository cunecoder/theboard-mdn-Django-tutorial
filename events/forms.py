from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'short_description', 'long_description', 'location', 'startdate', 'enddate', 'poster', 'category']
        widgets = {
            'startdate': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'enddate': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['startdate'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['enddate'].input_formats = ['%Y-%m-%dT%H:%M']