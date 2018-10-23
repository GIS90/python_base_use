from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^leads/', include('leads.urls')),
    url(r'^$', RedirectView.as_view(pattern_name='leads-list', permanent=False)),
)
