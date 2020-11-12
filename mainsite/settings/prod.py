from .base import *

DEBUG = False

# This can be changed if we want to limit the hosts that can connect to this app in production
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

DREAMS_INTERVENTION_API_ENDPOINT_CONF = {
    'api_user_name': 'api_user',
    'api_password': 'f6UbyBK97qRxN3Gp',
    'api_end_point': 'https://dreams.globalhealthapp.net/api/v1/interventions/'
}
