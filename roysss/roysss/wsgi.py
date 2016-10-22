"""
WSGI config for roysss project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roysss.settings")

from werkzeug.local import Local, LocalManager

_local = Local()
_local_manager = LocalManager([_local])

application = _local_manager.make_middleware(get_wsgi_application())

from roysss import _request_ctx_stack

_request_ctx_stack.push(application)
