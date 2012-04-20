from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
import logging
def staff_required(func):
    def inner(request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            if request.META['REQUEST_URI'] == '/':
                request.should_redirect = True
                return func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden('You do not have access to this resource')
        else:
            return func(request, *args, **kwargs)
    return inner
