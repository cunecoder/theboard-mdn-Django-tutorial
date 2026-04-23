# This is where we add patterns as we build the application
from django.urls import path
from . import views

# Personal notes: path contains: path('URLpattern', view.fnc, name))
urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail')
]