from django.shortcuts import render
from django.views import generic
from .models import Event, Category

# Create your views here.
def index(request):
    """View function for home page of the site."""

    # Personal Notes: This is how you get items from the database onto a page. You do your stuff here, any calcs and fncs (I think),
    #                 and then you pass it into the return render(...). On the html page, you can access the variables by how you named
    #                 them here by doing using DOUBLE curly brackets like so: {{ my_variable }}
    # Generate counts of some of the main objects
    num_events = Event.objects.all().count()

    # Find the number of Events where the category is "Sports"
    num_sport_events = Event.objects.filter(category__name="Sports").count()
    
    # Number of Events where category is "Social"
    num_social_events = Event.objects.filter(category__name="Social").count()

    # Left side: var name in HTML (var_name you use in the .html files)
    # Right side: var name in this Python views file
    context = {
        'num_events': num_events,
        'num_sport_events': num_sport_events,
        'num_social_events': num_social_events,
    }

    # Redner the HTML template index.html with the data in the context var
    return render(request, 'index.html', context=context)

class EventListView(generic.ListView):
    model = Event
    # Only displays 10 events per page. Later, I might want to have an endless stream of events.
    paginate_by = 10

    # My own name for the list as a template var
    context_object_name = 'event_list'

    # Note: You can customize this to be a specific query set. Be creative! ;-)
    queryset = Event.objects.all()
    # Template name goes along with the query set
    template_name = 'events/event_list.html'

class EventDetailView(generic.DetailView):
    model = Event
