"""ASGI entry point for the prime project.

Author: kawas8516 <https://github.com/kawas8516>
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prime.settings")

application = get_asgi_application()
