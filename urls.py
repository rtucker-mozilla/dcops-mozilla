from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", "work_log.views.index", name='home'),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^work_log/", include("work_log.urls")),
    url(r"^calendar/", include("dcops_calendar.urls")),
    url(r"^shipping/", include("dcops_shipping.urls")),
    url(r"^search/", include("dcops_search.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
