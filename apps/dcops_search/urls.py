from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^$", 'dcops_search.views.index', name="dcops_search_index"),
)
