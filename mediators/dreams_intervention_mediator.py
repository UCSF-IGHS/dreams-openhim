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
            client_id = self.get_value_or_none(data, "client_id")
            dreams_id = self.get_value_or_none(data, "dreams_id")
            user = self.get_value_or_none(data, "username")
            implementing_partner = self.get_value_or_none(data, "implementing_partner")

            converted_json_dictionary = []

            for odk_intervention in data["g_intervention"]:
                intervention = {
                    "intervention_date": self.get_value_or_none(odk_intervention, "intervention_date"),
                    "client": client_id,
                    "dreams_id": dreams_id,
                    "created_by": user,
                    "implementing_partner": implementing_partner,
                    "intervention_type": self.get_value_or_none(odk_intervention, "intervention_type"),
                    "name_specified": self.get_value_or_none(odk_intervention, "other_interventions"),
                    "pregnancy_test_result": self.get_value_or_none(odk_intervention, "pregnancy_test_reults"),
                    "hts_result": self.get_value_or_none(odk_intervention, "hts_results"),
                    "client_ccc_number": self.get_value_or_none(odk_intervention, "client_ccc_number"),
                    "date_linked_to_ccc": None,
                    "number_of_sessions_attended": self.get_value_or_none(odk_intervention,
                                                                          "number_of_sessions_attended"),
                    "comment": self.get_value_or_none(odk_intervention, "comments"),
                    "external_organisation": self.get_value_or_none(odk_intervention, "external_organization"),
                    "external_organisation_other": self.get_value_or_none(odk_intervention,
                                                                          "other_external_organization"),
                }
                converted_json_dictionary.append(intervention)

            json_response = json.dumps(converted_json_dictionary)
            return json_response

    @staticmethod
    def get_value_or_none(source: dict, key: str):
        try:
            return source[key]
        except KeyError:
            return None
