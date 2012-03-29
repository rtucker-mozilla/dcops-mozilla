from django import forms
import models
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from itertools import chain
class WorkLogForm(forms.ModelForm):
    completion_date = forms.DateField(label='Date Completed')
    expected_completion_date = forms.DateField(label='Expected Completion', required=False)
    completion_date = forms.DateField(label='Completion Date', required=False)
    start_date = forms.DateField(label='Start Date', required=False)
    class Meta:
        model = models.WorkLog
        exclude= ('user')
DEPENDS_CHOICES = (
        (1,'Depends On'),
        (2,'Blocks'),
        )
class CustomBaseInlineFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(CustomBaseInlineFormset, self).__init__(*args, **kwargs)
        id = kwargs['instance'].id
        other_queryset = models.Depends.objects.filter(issue_id=id)
        self.queryset = list(chain(self.queryset, other_queryset))
        self.queryset = None
    def is_valid(self):
        return super(CustomBaseInlineFormset, self).is_valid() and not any([bool(e) for e in self.errors])
    def clean(self):
        super(CustomBaseInlineFormset, self).clean()

DependsFormset = inlineformset_factory(models.WorkLog, 
    models.Depends, 
    can_delete=True,
    formset=CustomBaseInlineFormset,
    extra=3)
