from django.http import HttpResponseRedirect, HttpResponseForbidden
def staff_required(func):
    def inner(request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            return HttpResponseForbidden('You do not have access to this resource')
        else:
            return func(request, *args, **kwargs)
    return inner
