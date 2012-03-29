from django.conf import settings
from apps.work_log.models import DataCenter
 
def datacenters(request):
    return {
        'data_centers' : DataCenter.objects.all()
    }
