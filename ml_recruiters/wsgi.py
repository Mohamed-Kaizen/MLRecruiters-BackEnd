"""
WSGI config for ml_recruiters project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ml_recruiters.settings")

application = get_wsgi_application()
