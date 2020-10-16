import json
from django.test import TestCase

from mediators.dreams_intervention_mediator import DreamsInterventionMediator


class DreamsInterventionMediatorTestCase(TestCase):
    def setUp(self):
        self.odk_json = {
          "token": "Authorization: Basic ZHJlYW1zLW9kazpkcmVhbXMtb2Rr",
          "content": "record",
          "formId": "DREAMS_Interventions_Form",
          "formVersion": "2019622",
          "data": [
            {
              "*meta-instance-id*": "uuid:6cd3db4a-87ec-4288-98b3-d023c155fe1f",
              "*meta-model-version*": 2019622,
              "*meta-ui-version*": None,
              "*meta-submission-date*": "2020-10-16T09:03:35.568+03",
              "*meta-is-complete*": True,
              "*meta-date-marked-as-complete*": "2020-10-16T09:03:35.568+03",
              "start": "2020-10-16T09:01:44.050+03",
              "end": "2020-10-16T09:03:30.002+03",
              "deviceid": "339ac12a218aca44",
              "username": "jmacharia",
              "form_date_time": "2020-10-16",
              "implementing_partner": "3",
              "dreams_id": "2/1255/852",
              "n_confirmation": None,
              "client_id": "8637",
              "c_client_name": "SJO",
              "n_client_name": None,
              "c_Implemeneting_partner": "KCCB KARP",
              "n_Implemeneting_partner": None,
              "c_ward": "Gembe",
              "n_ward": None,
              "c_doe": "02/07/2016",
              "n_doe": None,
              "c_dob": "04/05/2006",
              "n_dob": None,
              "AGYW_details": "1",
              "n_AGYW_details": None,
              "g_intervention": [
                {
                  "intervention_type": "1001",
                  "c_behavioural_1": "MLRC 2017-06-30",
                  "c_behavioural_2": "MLRC 2017-06-30",
                  "c_behavioural_3": "MLRC 2017-06-30",
                  "n_behavioural": None,
                  "behavioural": "5",
                  "external_organization": "2",
                  "external_organ_interventions": None,
                  "other_external_organ_interventions": None,
                  "other_behavioural": None,
                  "behavioural_date": "2020-10-16",
                  "c_behavioural_date": "16/10/20",
                  "behavioural_comments": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "biomedical": None,
                  "biomedical_external_organization": None,
                  "biomedical_external_organ_interventions": None,
                  "other_biomedical": None,
                  "hts_result": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "biomedical_date": None,
                  "c_biomedical_date": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "post_gbv": None,
                  "gbv_external_organization": None,
                  "gbv_external_organ_interventions": None,
                  "post_gbv_date": None,
                  "c_post_gbv_date": None,
                  "post_gbv_comments": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "social_protection": None,
                  "social_external_organization": None,
                  "social_external_organ_interventions": None,
                  "social_protection_date": None,
                  "c_social_protection_date": None,
                  "social_protection_comments": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "other_interventions": None,
                  "other_external_organization": None,
                  "other_date": None,
                  "c_other_date": None,
                  "number_of_sessions_attended": None,
                  "other_comments": None
                }
              ],
              "comment_additional_services": None,
              "person_updating": "James",
              "date_updated": "2020-10-16",
              "c_date_updated": "16/10/20",
              "comments_notes": None,
              "instanceID": "uuid:6cd3db4a-87ec-4288-98b3-d023c155fe1f",
              "instanceName": "DREAMS INTERVENTION 3 2/1255/852 James"
            }
          ]
        }

    def test_convert_to_dream_intervention_api_json_returns_correct_data(self):
        mediator = DreamsInterventionMediator()
        converted_json_str = mediator.convert_to_dream_intervention_api_json(self.odk_json)
        self.assertIsNotNone(converted_json_str)

        converted_json = json.loads(converted_json_str)
        self.assertEqual(1, len(converted_json))

        for intervention in converted_json:
            self.assertEqual(intervention["intervention_date"], "2020-10-16")
            self.assertEqual(intervention["client_id"], "8637")
            self.assertEqual(intervention["dreams_id"], "2/1255/852")
