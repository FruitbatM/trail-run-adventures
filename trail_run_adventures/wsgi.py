import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'trail_run_adventures.settings')

application = get_wsgi_application()
