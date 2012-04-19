from work_log.models import WorkLog, Priority, DataCenter, WorkLogStatus
from django.contrib import admin
 
admin.site.register(Priority)
admin.site.register(WorkLog)
admin.site.register(WorkLogStatus)
admin.site.register(DataCenter)
