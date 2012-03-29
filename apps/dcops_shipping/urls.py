from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^$", 'dcops_shipping.views.index', name="dcops_shipping_index"),
    url(r"^edit/(?P<id>\d+)[/]", 'dcops_shipping.views.edit', name="dcops_shipping_edit"),
    url(r"^create[/]$", 'dcops_shipping.views.create', name="dcops_shipping_create"),
)    
                                                                                                                                                                                                   

