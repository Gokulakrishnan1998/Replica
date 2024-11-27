"""
WSGI config for jira_replica project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import sys
import os

project_path = '/home/Gokulakrishnan/replica'
if project_path not in sys.path:
    sys.path.append(project_path)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jira_replica.settings')

application = get_wsgi_application()
