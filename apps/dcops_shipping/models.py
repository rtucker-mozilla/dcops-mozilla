from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from dcops.apps.work_log.models import DataCenter, WorkLog

class Shipper(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    url = models.CharField(max_length=255, blank=False, null=False)
    def __unicode__(self):
        return self.name


DIRECTION_CHOICES = (
        (1,'Inbound'),
        (2,'Outbound'),
        )
class Shipment(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    shipper = models.ForeignKey('Shipper')
    signed_for_by = models.CharField(max_length=255, blank=True, null=True)
    tracking_number = models.CharField(max_length=255, blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    expected_arrival_date = models.DateField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    direction = models.IntegerField(blank=False, null=False, choices = DIRECTION_CHOICES)
    data_center = models.ForeignKey(DataCenter, blank=True, null=True, default=0)
    delivered = models.BooleanField(default=0)
    notes = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name

class Depends(models.Model):
    issue_id = models.IntegerField(blank=False, null=False)                                   
    shipment = models.ForeignKey('Shipment')
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.issue_id not in [l.id for l in WorkLog.objects.all()]:
            raise ValidationError('Issue ID not found %s' % self.issue_id)
