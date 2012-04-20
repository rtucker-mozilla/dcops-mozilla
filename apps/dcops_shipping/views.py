from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import staff_required
from django.core.urlresolvers import reverse
import forms, models
from decorators import staff_required

@staff_required
def index(request):
    list = models.Shipment.objects.all()
    return render_to_response('dcops_shipping/index.html', {'list':list}, RequestContext(request) )

@staff_required
def edit(request, id):
    instance = get_object_or_404(models.Shipment, id=id)
    if request.method == "POST":
        form = forms.ShipmentForm(request.POST, instance=instance)
        if form.is_valid():
            f = form.save(commit=False)
            depends_form = forms.DependsFormset(request.POST, instance=f)
            if depends_form.is_valid():
                f.user = request.user
                f.save()
                depends_form.save()
                return HttpResponseRedirect(reverse('dcops_shipping_index'))
        else:
            depends_form = forms.DependsFormset(request.POST, instance=instance)
    else:
        form = forms.ShipmentForm(instance=instance)
        depends_form = forms.DependsFormset(instance=instance)

    return render_to_response('dcops_shipping/edit.html', {'form':form, 'depends_form':depends_form}, context_instance=RequestContext(request) )


@staff_required
def create(request):
    if request.method == "POST":
        form = forms.ShipmentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            depends_form = forms.DependsFormset(request.POST, instance=f)
            if depends_form.is_valid():
                f.user = request.user
                f.save()
                depends_form.save()
                return HttpResponseRedirect(reverse('dcops_shipping_index'))
        else:
            depends_form = forms.DependsFormset(request.POST)
    else:
        form = forms.ShipmentForm()
        depends_form = forms.DependsFormset()

    return render_to_response('dcops_shipping/create.html', {'form':form, 'depends_form':depends_form}, context_instance=RequestContext(request) )
