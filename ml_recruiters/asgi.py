"""
ASGI config for ml_recruiters project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ml_recruiters.settings")

application = get_asgi_application()
