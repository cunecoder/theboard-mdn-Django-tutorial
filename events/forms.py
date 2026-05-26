from django import forms
from django.utils import timezone
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

    def clean(self):
        """Validate that start date comes before the end date."""
        cleaned_data = super().clean()
        start = cleaned_data.get('startdate')
        end = cleaned_data.get('enddate')
        now = timezone.now()

        # Check if a date is not in the past.
        if start and start < now:
            raise forms.ValidationError("Start date cannot be in the past, silly goose!")

        # Check if the start date comes before the end date.
        if start and end and start > end:
            raise forms.ValidationError("Start date must be before end date, silly goose!")
        
        return cleaned_data