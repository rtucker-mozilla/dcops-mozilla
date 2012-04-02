from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^$", 'work_log.views.index', name="work_log_index"),
    url(r"^train_schedule[/]$", 'work_log.views.train_schedule', name="work_log_train_schedule"),
    url(r"^mine[/]$", 'work_log.views.mine', name="work_log_mine"),
    url(r"^unassigned[/]$", 'work_log.views.unassigned', name="work_log_unassigned"),
    url(r"^datacenter/(?P<id>\d+)[/]$", 'work_log.views.data_center', name="work_log_data_center"),
    url(r"^create[/]", 'work_log.views.create', name="work_log_create"),
    url(r"^edit/(?P<id>\d+)[/]", 'work_log.views.edit', name="work_log_edit"),
)
