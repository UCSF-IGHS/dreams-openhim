from mediators.registration.auth import Auth
from mediators.registration.mediator_registration import MediatorRegistration
from mediators.registration.heartbeat import Heartbeat

from apscheduler.schedulers.background import BackgroundScheduler


class Main:
    def __init__(self, **kwargs):
        self.auth = Auth(kwargs['options'])
        self.mediator_registration = MediatorRegistration(
            auth=self.auth,
            conf=kwargs['conf'],
            options={
                'mediators_url': "{}/mediators".format(kwargs['options']['apiURL']),
                'verify_cert': kwargs['options']['verify_cert'],
                'force_config': kwargs['options']['force_config']
            }
        )
        self.heartbeat = Heartbeat(
            self.auth,
            options=kwargs['options'],
            conf=kwargs['conf'],
            scheduler=BackgroundScheduler()
        )

    def authenticate(self):
        return self.auth.authenticate()
    
    def gen_auth_headers(self):
        return self.auth.gen_auth_headers()
    
    def register_mediator(self):
        self.mediator_registration.run()
    
    def activate_heartbeat(self):
        return self.heartbeat.activate()
    
    def deactivate_heartbeat(self):
        return self.heartbeat.deactivate()
    
    def fetch_config(self):
        return self.heartbeat.fetch_config()