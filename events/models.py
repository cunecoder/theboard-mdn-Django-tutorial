from django.db import models
from django.utils import timezone
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID
from django.conf import settings

# Create your models here.
class Category(models.Model):
    """ Model representing a category for filtering events."""
    name = models.CharField(max_length=50, unique=True)
    # Slug field is used for URLS like this: /categories/sports
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    """Model representing an Event."""

    # Fields
    title = models.CharField(unique=True, null=False, blank=False, max_length=50)
    short_description = models.TextField(max_length=200, null=False,  blank=False, help_text='Enter a short description that would fit on the events display.')
    long_description = models.TextField(max_length=500, blank=True)
    location = models.CharField(unique=True, blank=False, max_length=50)
    startdate = models.DateTimeField(default=timezone.now, null=False,  blank=False)
    enddate = models.DateTimeField(null=True, blank=True)
    poster = models.ImageField(upload_to='posters/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    # Model methods
    def __str__(self):
        """String for representing the Event object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a particular Event instance."""
        # The return statement will allow a link to a url with each event's id. Ex: events/3/
        # 'Give me the URL to view THIS event instance'
        # In urls.py: path("events/<int:id>/", views.event_detail, name="event-detail")
        return reverse('event-detail', args=[str(self.id)])
