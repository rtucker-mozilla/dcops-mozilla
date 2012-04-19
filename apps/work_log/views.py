# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
import models, forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import logging


@login_required
def index(request):
    list = models.WorkLog.objects.all()
    return render_to_response('work_log/index.html', {'list':list}, RequestContext(request) )

@login_required
def mine(request):
    list = models.WorkLog.objects.filter(assigned_to=request.user)
    return render_to_response('work_log/index.html', {'list':list}, RequestContext(request) )
@login_required
def unassigned(request):
    list = models.WorkLog.objects.filter(assigned_to=None)
    return render_to_response('work_log/index.html', {'list':list}, RequestContext(request) )
@login_required
def data_center(request, id):
    list = models.WorkLog.objects.filter(dc=id)
    return render_to_response('work_log/index.html', {'list':list}, RequestContext(request) )
def train_schedule(request):
    list = models.TrainSchedule.objects.all()
    return render_to_response('work_log/train_schedule.html', {'list':list}, RequestContext(request) )
@login_required
def edit(request, id):
    instance = get_object_or_404(models.WorkLog, id=id)
    if request.method == "POST":
        form = forms.WorkLogForm(request.POST, instance=instance)                                                                                                                                          
        if form.is_valid():
            f = form.save(commit=False)
            depends_form = forms.DependsFormset(request.POST, instance=f)
            logging.info("Outside")
            logging.info(depends_form)
            if depends_form.is_valid():
                logging.info("here")
                f.user = request.user
                depends_form.save()
                f.save()
                return HttpResponseRedirect(reverse('work_log_index'))
            else:
                logging.info("not valid")
                for error in depends_form.errors:
                    logging.info(error)
        else:
            depends_form = forms.DependsFormset(request.POST, instance=instance)
    else:
        form = forms.WorkLogForm(instance=instance)
        depends_form = forms.DependsFormset(instance=instance)

    return render_to_response('work_log/edit.html', {'form':form, 'depends_form':depends_form}, context_instance=RequestContext(request) )

@login_required
def create(request):
    if request.method == "POST":
        form = forms.WorkLogForm(request.POST)                                                                                                                                          
        if form.is_valid():
            f = form.save(commit=False)
            depends_form = forms.DependsFormset(request.POST, instance=f)
            if depends_form.is_valid():
                f.user = request.user
                f.save()
                depends_form.save()
                return HttpResponseRedirect(reverse('work_log_index'))
        else:
            depends_form = forms.DependsFormset(request.POST)
    else:
        form = forms.WorkLogForm()
        depends_form = forms.DependsFormset()

    return render_to_response('work_log/create.html', {'form':form, 'depends_form':depends_form}, RequestContext(request) )

