# This is where we add patterns as we build the application
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    EventDetailView, EventUpdateView, EventCreateView, EventDeleteView
)

# Personal notes: path contains: path('URLpattern', view.fnc, name))
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.EventListView.as_view(), name='events'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]