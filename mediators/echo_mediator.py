from mediators.registration.auth import Auth
from copy import copy
from mediators.registration.mediator_registration import MediatorRegistration
from django.conf import settings


class EchoMediator:
    def __init__(self):
        self.options = copy(settings.OPENHIM_OPTIONS)
        self.mediator_conf = copy(settings.ECHO_MEDIATOR_CONF)

    def register(self):
        registration = MediatorRegistration(
            options=self.options,
            auth=Auth({'verify_cert': self.options['verify_cert'], 'apiURL': self.options['apiURL'],
                       'username': self.options['username'], 'password': self.options['password']}),
            conf=self.mediator_conf
        )
        registration.run()
