import json
from copy import copy
from unittest.mock import patch

import requests
from django.conf import settings
from django.test import TestCase
from requests import Session
from requests.auth import HTTPBasicAuth

from mediators.dreams_intervention_mediator import DreamsInterventionMediator
from mediators.views.dreams_intervention_mediator_api_view import DreamsInterventionMediatorAPIView


class DreamsInterventionMediatorTestCase(TestCase):
    def setUp(self):
        self.odk_json = {
            "token": "",
            "content": "record",
            "formId": "DREAMS_Interventions_Form",
            "formVersion": "2019622",
            "data": [
              {
                "*meta-instance-id*": "uuid:5b8430c0-7f0f-4f8e-ae94-d7055fbf355d",
                "*meta-model-version*": 2019622,
                "*meta-ui-version*": None,
                "*meta-submission-date*": "2020-10-24T11:13:11.473+03",
                "*meta-is-complete*": True,
                "*meta-date-marked-as-complete*": "2020-10-24T11:13:11.473+03",
                "start": "2020-10-24T11:08:48.831+03",
                "end": "2020-10-24T11:13:01.198+03",
                "deviceid": "339ac12a218aca44",
                "username": "jmacharia",
                "form_date_time": "2020-10-24",
                "implementing_partner": "5",
                "dreams_id": "5/1205/17",
                "n_confirmation": None,
                "client_id": "594774",
                "c_client_name": "JAM",
                "n_client_name": None,
                "c_Implemeneting_partner": "Henry Jackson Foundation",
                "n_Implemeneting_partner": None,
                "c_ward": "North Seme",
                "n_ward": None,
                "c_doe": "26/02/2019",
                "n_doe": None,
                "c_dob": "01/01/1999",
                "n_dob": None,
                "AGYW_details": "1",
                "n_AGYW_details": None,
                "age": None,
                "c_behavioural_1": "SHUGA II 2020-08-21",
                "c_behavioural_2": "SHUGA II 2020-08-21",
                "c_behavioural_3": "SHUGA II 2020-08-21",
                "n_behavioural": None,
                "c_biomedical_1": "HTS (Client) 2019-02-26",
                "c_biomedical_2": "Condom Education and Demo 2019-02-26",
                "c_biomedical_3": "Condom Education and Demo 2019-02-26",
                "n_biomedical": None,
                "c_post_gbv_1": "Physical Violence - PSS 2020-07-14",
                "c_post_gbv_2": "Physical Violence - Trauma Counselling 2020-07-14",
                "c_post_gbv_3": "Physical Violence - Trauma Counselling 2020-07-14",
                "n_post_gbv": None,
                "c_social_protection_1": "Economic Strengthening - Financial Capabilities Training 2020-06-24",
                "c_social_protection_2": "Economic Strengthening - Financial Capabilities Training 2020-06-24",
                "c_social_protection_3": "Physical Violence - Trauma Counselling 2020-07-14",
                "n_social_protection": None,
                "c_other_intervention_1": "Social Asset Building - Number of Sessions Attended 2019-02-26",
                "c_other_intervention_2": "Cash Transfer 2019-03-26",
                "c_other_intervention_3": "Social Asset Building - Number of Sessions Attended 2019-04-27",
                "n_other": None,
                "g_given_intervention": [
                  {
                    "intervention_category": "1001",
                    "intervention_types": "1002",
                    "other_intervention_types": None,
                    "external_organization": "1",
                    "external_organization_name": "1",
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "1001",
                    "intervention_types": "1008",
                    "other_intervention_types": "Test",
                    "external_organization": "1",
                    "external_organization_name": "4",
                    "other_external_organization_name": "Test",
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "2001",
                    "intervention_types": "2002",
                    "other_intervention_types": None,
                    "external_organization": "2",
                    "external_organization_name": None,
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": "201",
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "2001",
                    "intervention_types": "2006",
                    "other_intervention_types": None,
                    "external_organization": "1",
                    "external_organization_name": "3",
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": "12345",
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "3001",
                    "intervention_types": "5007",
                    "other_intervention_types": None,
                    "external_organization": "2",
                    "external_organization_name": None,
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": "Test"
                  },
                  {
                    "intervention_category": "3001",
                    "intervention_types": "5010",
                    "other_intervention_types": None,
                    "external_organization": "1",
                    "external_organization_name": "2",
                    "other_external_organization_name": None,
                    "referral": "Test",
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "4001",
                    "intervention_types": "3013",
                    "other_intervention_types": None,
                    "external_organization": "2",
                    "external_organization_name": None,
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "4001",
                    "intervention_types": "3024",
                    "other_intervention_types": "Test",
                    "external_organization": "1",
                    "external_organization_name": "2",
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "5001",
                    "intervention_types": "4018",
                    "other_intervention_types": None,
                    "external_organization": "1",
                    "external_organization_name": "2",
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": "Test"
                  },
                  {
                    "intervention_category": "4001",
                    "intervention_types": "3014",
                    "other_intervention_types": None,
                    "external_organization": "2",
                    "external_organization_name": None,
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "5001",
                    "intervention_types": "4005",
                    "other_intervention_types": None,
                    "external_organization": "1",
                    "external_organization_name": "2",
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": None,
                    "comments": None
                  },
                  {
                    "intervention_category": "3001",
                    "intervention_types": "5008",
                    "other_intervention_types": None,
                    "external_organization": "1",
                    "external_organization_name": "2",
                    "other_external_organization_name": None,
                    "referral": None,
                    "intervention_date": "2020-10-24",
                    "c_intervention_date": "0",
                    "n_intervention_date": None,
                    "hts_results": None,
                    "client_ccc_number": None,
                    "pregnancy_test_reults": None,
                    "number_of_sessions_attended": 100,
                    "comments": "Test"
                  }
                ],
                "comment_additional_services": "Test",
                "person_updating": "James test",
                "date_updated": "2020-10-24",
                "c_date_updated": "24/10/20",
                "comments_notes": None,
                "instanceID": "uuid:5b8430c0-7f0f-4f8e-ae94-d7055fbf355d",
                "instanceName": "DREAMS INTERVENTION 5 5/1205/17 James test"
              }
            ]
          }
        self.converted_json = [{
            "intervention_date": "2020-10-01",
            "client": 1,
            "dreams_id": "2/2/2222",
            "intervention_type": 1002,
            "name_specified": None,
            "hts_result": 201,
            "pregnancy_test_result": 101,
            "client_ccc_number": None,
            "date_linked_to_ccc": None,
            "number_of_sessions_attended": None,
            "comment": None,
            "created_by": "api_user",
            "implementing_partner": 6,
            "external_organisation": None,
            "external_organisation_other": None
        }]

    def test_convert_to_dream_intervention_api_json_returns_correct_data(self):
        mediator = DreamsInterventionMediator()
        converted_json_str = mediator.convert_to_dream_intervention_api_json(self.odk_json)
        self.assertIsNotNone(converted_json_str)

        converted_json = json.loads(converted_json_str)
        self.assertEqual(12, len(converted_json))

        for intervention in converted_json:
            self.assertEqual(intervention["client"], "594774")
            self.assertEqual(intervention["dreams_id"], "5/1205/17")

        intervention_date_for_the_first_intervention = converted_json[0]["intervention_date"]
        self.assertEqual(intervention_date_for_the_first_intervention, "2020-10-24")

    def test_get_value_or_none_returns_none(self):
        converted_json = json.loads("{ \"key\": null  }")
        returned_value = DreamsInterventionMediator.get_value_or_none(converted_json, "key")
        self.assertIsNone(returned_value)

    def test_get_value_or_none_returns_value(self):
        converted_json = json.loads("{ \"key\": 4  }")
        returned_value = DreamsInterventionMediator.get_value_or_none(converted_json, "key")
        self.assertEqual(4, returned_value)

    def test_get_value_or_none_returns_array(self):
        converted_json = json.loads("{ \"key\": [{\"key1\": 1}, {\"key2\": 22}]  }")
        returned_value = DreamsInterventionMediator.get_value_or_none(converted_json, "key")
        self.assertEqual(2, len(returned_value))
        self.assertEqual(22, returned_value[1]['key2'])

    @patch('requests.post')
    def test_call_dreams_interventions_api(self, mock_request):
        api_conf = copy(settings.DREAMS_INTERVENTION_API_ENDPOINT_CONF)
        mock_request.get.content.return_value = '{status_code: 200}'
        mock_request.path_url = api_conf['api_end_point']
        mock_request.auth = HTTPBasicAuth(api_conf['api_user_name'], api_conf['api_password'])
        mock_request.method = 'POST'
        mock_request.return_value.status_code = 201
        mock_request.return_value.body = json.dumps({"status": "success"})

        mediator_view = DreamsInterventionMediatorAPIView()
        for intervention in self.converted_json:
            api_response = mediator_view.call_dreams_interventions_api(json.dumps(intervention))
            self.assertIsNotNone(api_response)

    @patch.object(Session, 'send')
    def test_generate_orchestration_results(self, mock_request):
        api_conf = copy(settings.DREAMS_INTERVENTION_API_ENDPOINT_CONF)
        mock_request.path = api_conf['api_end_point']
        mock_request.method = 'POST'
        mock_request.querystring = None
        mock_request.return_value.status_code = 200
        mock_request.headers._store = {'content-type': 'application/json', 'content-length': 200}
        mock_request.return_value.content = json.dumps(self.converted_json)

        request = requests.Request(method='POST', url=api_conf['api_end_point'], data=json.dumps(self.converted_json),
                                   json=self.converted_json, headers={'content-type': 'application/json', })

        prepared_request = request.prepare()
        prepared_request.data = self.converted_json

        mock_request.return_value.request = prepared_request

        session = requests.Session()
        response = session.send(prepared_request)
        self.assertEqual(response.status_code, 200)

        mediator_view = DreamsInterventionMediatorAPIView()
        response_to_him = mediator_view.generate_orchestration_results(prepared_request, response)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response_to_him['x-mediator-urn'])
        self.assertTrue(response_to_him['status'] in
                        ['Processing', 'Failed', 'Completed', 'Successful', 'Completed with error(s)'])
        self.assertIsNotNone(response_to_him['response'])
        self.assertIsNotNone(response_to_him['orchestrations'])
        self.assertIsNotNone(response_to_him['properties'])

    def test_concatenate_comments(self):
        string_1 = "test"
        string_2 = "123"

        concatenation = DreamsInterventionMediator.concatenate_comments(string_1, string_2)
        self.assertEqual("test; 123", concatenation)

        concatenation = DreamsInterventionMediator.concatenate_comments(string_1, None)
        self.assertEqual("test", concatenation)

        concatenation = DreamsInterventionMediator.concatenate_comments(None, string_2)
        self.assertEqual("123", concatenation)

        concatenation = DreamsInterventionMediator.concatenate_comments(None, None)
        self.assertIsNone(concatenation)
