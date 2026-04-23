from django.shortcuts import render
from .models import Event, Category

# Create your views here.
def index(request):
    """View function for home page of the site."""

    # Generate counts of some of the main objects
    num_events = Event.objects.all().count()

    context = {
        'num_events': num_events,
    }

    # Redner the HTML template index.html with the data in the context var
    return render(request, 'index.html', context=context)