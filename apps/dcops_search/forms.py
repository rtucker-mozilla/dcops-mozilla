from django import forms
import models
from dcops.apps.dcops_shipping.models import Shipment
from dcops.apps.work_log.models import DataCenter, WorkLog, Priority
from django.contrib.auth.models import User

DC_CHOICES = [('', 'All')] + [(m.id, m.name) for m in DataCenter.objects.all()]
PRIORITY_CHOICES = [('', 'All')] + [(m.id, m.name) for m in Priority.objects.all()]
ASSIGNED_TO_CHOICES = [('', 'All')] + [(m.id, m.username) for m in User.objects.filter(id__gt=1)]
SEARCH_SCOPES = (
            ('', 'All'),
            ('1', 'Work Log Entries'),
            ('2', 'Shipments'),
            )
class SearchForm(forms.Form):
   search_term = forms.CharField(max_length=100)
   data_center = forms.ChoiceField(choices=DC_CHOICES, required=False)
   priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False)
   assigned_to = forms.ChoiceField(choices=ASSIGNED_TO_CHOICES, required=False)
   search_scope = forms.ChoiceField(choices=SEARCH_SCOPES, required=False)

