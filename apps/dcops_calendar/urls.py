from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^expected_completion[/]$", 'dcops_calendar.views.expected_completion', name="dcops_calendar_expected_completion"),
    url(r"^expected_start[/]$", 'dcops_calendar.views.expected_start', name="dcops_calendar_expected_start"),
    url(r"^shipping/]$", 'dcops_calendar.views.shipping', name="dcops_calendar_shipping"),
)
