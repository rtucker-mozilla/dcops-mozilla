# Create your views here.
from work_log.models import WorkLog
from dcops_shipping.models import Shipment
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
import logging
from django.core.urlresolvers import reverse
from django.db.models import Count
from custom_decorators.decorators import staff_required

@staff_required
def expected_start(request, instance=None):
    pass

@staff_required
def expected_completion(request, instance=None):
    events = WorkLog.objects.all()
    out_string = get_event_string(events, 'expected_completion_date')
    return render_to_response('dcops_calendar/index.html', {'title': 'Expected Completion Calendar', 'events':out_string, }, context_instance=RequestContext(request))

@staff_required
def expected_start(request, instance=None):
    events = WorkLog.objects.all()
    out_string = get_event_string(events, 'start_date')
    return render_to_response('dcops_calendar/index.html', {'title': 'Expected Start Date Calendar', 'events':out_string, }, context_instance=RequestContext(request))

@staff_required
def shipping(request, instance=None):
    events = Shipment.objects.all().group_by('arrival_date', 'data_center')
    logging.info(events)

    out_string = get_event_string(events, 'shipping')
    return render_to_response('dcops_calendar/index.html', {'title': 'Shipping Calendar', 'events':out_string, }, context_instance=RequestContext(request))

def get_event_string(events, type):
    out_events = []
    for event in events:
        if type == 'start_date':
            out_events.append({
                'title': event.name,
                'id': event.id,
                'color': event.priority.color,
                'start': 'parse_date("%s")' % (str(event.start_date)),
                'end': 'parse_date("%s")' % (str(event.start_date)),
                })
        elif type == 'expected_completion_date':
            out_events.append({
                'title': event.name,
                'id': event.id,
                'color': event.priority.color,
                'start': 'parse_date("%s")' % (str(event.expected_completion_date)),
                'end': 'parse_date("%s")' % (str(event.expected_completion_date)),
                })
        elif type == 'shipping':
            out_events.append({
                'title': events['data_center__count'],
                'id': 'sadf',
                'color': 'blue',
                'start': 'parse_date("%s")' % (str(event.arrival_date)),
                'end': 'parse_date("%s")' % (str(event.arrival_date)),
                })
        event_count = len(out_events)
        counter = 0
        out_string = ""
        for event in out_events:
            out_string += "{url: '%s', title:\"%s\", start: %s, end: %s, color:'%s'}" % ( reverse('work_log_edit', args=[event['id']]), event['title'], event['start'], event['end'], event['color'])
            if counter + 1 < event_count:
                out_string = "%s," % out_string
            counter+=1
    out_string = "[%s]" % (out_string)
    return out_string
