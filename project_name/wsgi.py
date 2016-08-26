"""
WSGI config for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")

try:
  # at the moment, cloud debugger not supported for Python 3
  # https://cloud.google.com/debugger/docs/setting-up-python-on-app-engine
  import googleclouddebugger
  googleclouddebugger.AttachDebugger(
      version=os.environ.get('GAE_MODULE_VERSION', ''),
      module=os.environ.get('GAE_MODULE_NAME', ''),
  )
except ImportError:
  pass

application = get_wsgi_application()
