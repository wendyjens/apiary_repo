"""
WSGI config for apiary_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set it to use azure.py for production environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiary_project.azure')
application = get_wsgi_application()
