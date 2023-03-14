

import os

from django.core.asgi import get_asgi_application
import os
print(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nextTechnology.settings')

application = get_asgi_application()
