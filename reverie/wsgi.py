"""
WSGI config for reverie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

django_env = os.environ.get('django_env')

if not django_env:
    django_env = 'dev'

settings_module = "reverie.settings.{0}".format(django_env)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
