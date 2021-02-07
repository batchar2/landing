"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


# добавляю в пути проект
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chsite.settings')


application = get_wsgi_application()
