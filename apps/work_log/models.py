from django.db import models
from django.contrib.auth.models import User
from itertools import chain
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location="/var/www/dcops.mozilla.com/dcops/")
import settings
# Create your models here.
class DependencyManager(models.Manager):
    
    def depends_on(self):
        return self.get_query_set().depends_set.filter(direction=1)

    def blocks(self):
        return self.get_query_set().depends_set.filter(direction=2)
class TrainSchedule(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    train_date = models.DateField(blank=True, null=True)
    #file = models.FileField(storage=fs)
    file = models.FileField(upload_to='train')

    def __unicode__(self):
        return "%s - %s" % (self.name, self.train_date)

    def get_absolute_url(self):
        return "%s%s" % (settings.MEDIA_URL, self.file)

    def get_download_url(self):
        return "%s%s" % (settings.MEDIA_URL, self.file)

class WorkLog(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    created_on = models.DateField(auto_now_add=True)
    start_date = models.DateField(blank=True, null=True)
    expected_completion_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, blank=False, null=False)
    assigned_to = models.ForeignKey(User, blank=True, null=True, related_name='assigned_to')
    priority = models.ForeignKey('Priority')
    dc = models.ForeignKey('DataCenter')
    status = models.ForeignKey('WorkLogStatus', default=1)

    def get_blocks(self):
        ret_list = []
        for item in Depends.objects.filter(work_log=self).filter(direction=2):
            ret_list.append(item.issue_id)
        for item in Depends.objects.filter(issue_id=self.id).filter(direction=1):
            ret_list.append(item.work_log.id)
        ret_list= set(ret_list)
        return ret_list

    def get_depends(self):
        ret_list = []
        for item in Depends.objects.filter(work_log=self).filter(direction=1):
            ret_list.append(item.issue_id)
        for item in Depends.objects.filter(issue_id=self.id).filter(direction=2):
            ret_list.append(item.work_log.id)
        ret_list= set(ret_list)
        return ret_list

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'work_log'

        """
            Once I figure out how to edit the far end of a M2M relationship, I'll add this back in
        """
DEPENDS_CHOICES = (
        #(1,'Depends On'),
        (1,'Blocks'),
        (2,'Blocks'),
        )
class Depends(models.Model):
    issue_id = models.IntegerField(blank=False, null=False)
    direction = models.IntegerField(blank=False, null=False, choices = DEPENDS_CHOICES)
    work_log = models.ForeignKey('WorkLog')
    """def __init__(self, *args, **kwargs):
        pass"""
    def clean(self, *args, **kwargs):
        from django.core.exceptions import ValidationError
        if self.issue_id not in [l.id for l in WorkLog.objects.all()]:
            raise ValidationError('Issue ID not found %s' % self.issue_id)
        return super(Depends, self).clean(*args, **kwargs)

class DataCenter(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    color = models.CharField(max_length=128, blank=False, null=False, default='blue')
    def __unicode__(self):
        return self.name
    class Meta:
        pass

class Priority(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    color = models.CharField(max_length=128, blank=False, null=False)
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'work_log_priority'
class WorkLogStatus(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Work Log Statuses"

class Depends(models.Model):
    issue_id = models.IntegerField(blank=False, null=False)
    direction = models.IntegerField(blank=False, null=False, choices = DEPENDS_CHOICES)
    work_log = models.ForeignKey('WorkLog')
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.issue_id not in [l.id for l in WorkLog.objects.all()]:
            raise ValidationError('Issue ID not found %s' % self.issue_id)

class Blocks(models.Model):
    work_log = models.ForeignKey('WorkLog')

