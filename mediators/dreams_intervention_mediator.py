import json

from .auth import Auth
from copy import copy
from .mediator_registration import MediatorRegistration
from django.conf import settings


class DreamsInterventionMediator:
    def __init__(self):
        self.options = copy(settings.OPENHIM_OPTIONS)
        self.mediator_conf = copy(settings.DREAMS_INTERVENTION_MEDIATOR_CONF)

    def register(self):
        registration = MediatorRegistration(
            options=self.options,
            auth=Auth({'verify_cert': self.options['verify_cert'], 'apiURL': self.options['apiURL'],
                       'username': self.options['username'], 'password': self.options['password']}),
            conf=self.mediator_conf
        )
        registration.run()

    def convert_to_dream_intervention_api_json(self, odk_json):

        converted_json_dictionary = [{
            "intervention_date": "2020-10-01",
            "client_id": 1,
            "dreams_id": "2/2/2222",
            "intervention_type": 1002,
            "name_specified": None,
            "hts_result": 201,
            "pregnancy_test_result": 101,
            "client_ccc_number": None,
            "date_linked_to_ccc": None,
            "number_of_sessions_attended": None,
            "comment": None,
            "created_by": "admin",
            "implementing_partner": 6,
            "external_organization": None,
            "external_organization_other": None
        }]
        json_response = json.dumps(converted_json_dictionary)
        return json_response
