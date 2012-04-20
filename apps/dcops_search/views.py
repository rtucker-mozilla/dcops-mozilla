# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
import models, forms
from dcops.apps.work_log.models import WorkLog
from dcops.apps.dcops_shipping.models import Shipment
from django.core.urlresolvers import reverse
import logging
from django.db.models import Q
from custom_decorators.decorators import staff_required

@staff_required
def index(request):
    """
        We're using a request method of get with the top search bar. Display both sets of records for it
    """
    work_log_list = []
    shipment_log_list = []
    form = forms.SearchForm()
    search_scope = None
    if 'search_term' in request.GET:
        search_term = request.GET.get('search_term')
        work_log_list, shipment_log_list = process_search(search_term, data_center=None, search_scope = None)
        form = forms.SearchForm(request.GET)
    elif request.method == "POST":
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search_term = request.POST.get('search_term')
            data_center = request.POST.get('data_center')
            search_scope = request.POST.get('search_scope')
            priority = request.POST.get('priority')
            assigned_to = request.POST.get('assigned_to')
            work_log_list, shipment_log_list = process_search(search_term, data_center=data_center, search_scope=search_scope, priority=priority, assigned_to=assigned_to)
    return render_to_response('dcops_search/index.html', {'form':form, 'search_scope': search_scope, 'shipment_log_list':shipment_log_list, 'work_log_list':work_log_list}, RequestContext(request) )

def process_search(search_term, data_center=None, search_scope = None, priority=None, assigned_to=None):
    if search_scope == '':
        search_scope = None
    if data_center == '':
        data_center = None
    if priority == '':
        priority = None
    work_log_list = []
    shipment_log_list = []
    if search_scope is None or search_scope == '1':
        logging.info('here')
        shipment_log_list = []
        search_q = Q(name__icontains=search_term)
        search_q |= Q(notes__icontains=search_term)  
        if data_center:
            search_q &= Q(dc__id=data_center)  
        if priority:
            search_q &= Q(priority__id=priority)  
        if assigned_to:
            search_q &= Q(assigned_to__id=assigned_to)  

        work_log_list = WorkLog.objects.filter(search_q)
    if search_scope is None or search_scope == '2':
        search_q = Q(name__icontains=search_term)
        search_q |= Q(notes__icontains=search_term)  
        search_q |= Q(tracking_number__icontains=search_term)  
        if data_center:
            search_q &= Q(data_center__id=data_center)  
        else:
            search_q |= Q(data_center__name__icontains=search_term)  
        shipment_log_list = Shipment.objects.filter(search_q)
    return work_log_list, shipment_log_list

