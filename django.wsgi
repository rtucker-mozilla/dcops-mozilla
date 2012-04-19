"""
    This needs set to the absolute path for the virtualenv
"""
import os
VIRTUAL_ENV_ROOT = os.path.abspath(os.path.dirname(__file__))
ALLDIRS = ['%s/lib/python2.6/site-packages' % (VIRTUAL_ENV_ROOT),]

import os
import sys
import site

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr
prev_sys_path = list(sys.path)

for directory in ALLDIRS:
  site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path
"""
    This needs set to the activate script in the virtualenv
"""
activate_this = '%s/../bin/activate_this.py' % (VIRTUAL_ENV_ROOT)
execfile(activate_this, dict(__file__=activate_this))
from os.path import abspath, dirname, join
from site import addsitedir

sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.insert(0, abspath(dirname(__file__) ) )

from django.conf import settings
"""
    This needs set to the settings file
"""
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

#sys.path.insert(0, join(settings.PINAX_ROOT, "apps"))
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

