"""
WSGI config for velkozz_web_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from django.conf import settings

sys.path.append(os.path.join(settings.BASE_DIR, "apps"))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'velkozz_web_api.settings')

application = get_wsgi_application()
