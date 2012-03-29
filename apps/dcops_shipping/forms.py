from django import forms
from django.forms.models import inlineformset_factory
import models

class ShipperForm(forms.ModelForm):
    class Meta:
        model = models.Shipper

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = models.Shipment

DependsFormset = inlineformset_factory(models.Shipment, 
    models.Depends, 
    can_delete=True,
    extra=3)

