from django.utils import timezone
from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from events.models import Event, Category

# Create your tests here.
class EventTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        ''' Set up objects used by all test methods. '''
        category = Category.objects.create(name='Social')
        # Past event for testing
        Event.objects.create(
            title="Old Event",
            short_description="This happened already.",
            long_description="To be very honest with you, you're not invited. The event is done, go home.... It's over already....",
            location="Old Place",
            startdate=timezone.now() - timedelta(days=2),
            enddate=timezone.now() - timedelta(days=1),
            poster="media/posters/test_poster.jpg",
            category=category
        )

        # Future event for testing
        Event.objects.create(
            title="Future Event",
            short_description="This haas not yet happened.",
            long_description="This event is coming soon, so stay tuned...",
            location="The Future",
            startdate=timezone.now() + timedelta(days=1),
            enddate=timezone.now() + timedelta(days=2),
            poster="media/posters/test_poster.jpg",
            category=category
        )

    def test_past_events_not_displayed_on_events_dashboard(self):
        ''' Ensure past events are not being displayed. '''

        # This test was pretty much ChatGPT generated.
        response = self.client.get(reverse('events'))

        self.assertContains(response, "Future Event")
        self.assertNotContains(response, "Old Event")

    def test_past_event_detail_not_accessible(self):
        ''' Ensure past events cannot be viewed. '''

        # Note to self: this event is accessible because we created it in the setUpTestCase funtion!
        # Test pretty much from ChatGPT
        old_event = Event.objects.get(title='Old Event')
        response = self.client.get(
            reverse('event-detail', args=[old_event.id])
        )
        self.assertEqual(response.status_code, 404)