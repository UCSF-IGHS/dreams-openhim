import json

from mediators.registration.auth import Auth
from copy import copy
from mediators.registration.mediator_registration import MediatorRegistration
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

        for data in odk_json["data"]:
            client_id = data["client_id"]
            dreams_id = data["dreams_id"]
            user = data["username"]
            implementing_partner = data["implementing_partner"]

            converted_json_dictionary = []

            for odk_intervention in data["g_intervention"]:
                intervention = {
                    "intervention_date": odk_intervention["behavioural_date"],
                    "client_id": client_id,
                    "dreams_id": dreams_id,
                    "created_by": user,
                    "implementing_partner": implementing_partner,
                    "intervention_type": odk_intervention["intervention_type"],
                    "name_specified": odk_intervention["other_behavioural"],
                    "pregnancy_test_result": odk_intervention["pregnancy_test_reults"],
                    "hts_result": odk_intervention["hts_result"],
                    "client_ccc_number": odk_intervention["client_ccc_number"],
                    "date_linked_to_ccc": None,
                    "number_of_sessions_attended": odk_intervention["number_of_sessions_attended"],
                    "comment": odk_intervention["other_comments"],
                    "external_organization": odk_intervention["external_organization"],
                    "external_organization_other": odk_intervention["other_external_organization"],
                }
                converted_json_dictionary.append(intervention)

        # converted_json_dictionary = [
        #     {
        #             "intervention_date": "2020-10-01",
        #         "client_id": 1,
        #         "dreams_id": "2/2/2222",
        #             "intervention_type": 1002,
        #             "name_specified": None,
        #             "hts_result": 201,
        #             "pregnancy_test_result": 101,
        #             "client_ccc_number": None,
        #             "date_linked_to_ccc": None,
        #             "number_of_sessions_attended": None,
        #             "comment": None,
        #         "created_by": "admin",
        #         "implementing_partner": 6,
        #             "external_organization": None,
        #             "external_organization_other": None
        #     }
        # ]
            json_response = json.dumps(converted_json_dictionary)
            return json_response
