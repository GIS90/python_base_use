from django.conf.urls import patterns, url

from .views import LeadsList

urlpatterns = patterns(
    '',
    url(r'^$', LeadsList.as_view(), name='leads-list'),
)
