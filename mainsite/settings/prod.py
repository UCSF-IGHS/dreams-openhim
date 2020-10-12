from .base import *

DEBUG = False

# This can be changed if we want to limit the hosts that can connect to this app in production
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'