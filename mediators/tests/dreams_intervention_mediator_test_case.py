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
              "*meta-instance-id*": "uuid:9bca070c-9a48-4359-90c5-0642b5e1de05",
              "*meta-model-version*": 2019622,
              "*meta-ui-version*": None,
              "*meta-submission-date*": "2020-10-16T14:04:41.928+03",
              "*meta-is-complete*": True,
              "*meta-date-marked-as-complete*": "2020-10-16T14:04:41.928+03",
              "start": "2020-10-16T13:57:59.929+03",
              "end": "2020-10-16T14:04:33.850+03",
              "deviceid": "868355035691319",
              "username": "jmacharia",
              "form_date_time": "2020-10-16",
              "implementing_partner": "5",
              "dreams_id": "5/1204/17",
              "n_confirmation": None,
              "client_id": "1",
              "c_client_name": "AN",
              "n_client_name": None,
              "c_Implemeneting_partner": "Henry Jackson Foundation",
              "n_Implemeneting_partner": None,
              "c_ward": "East Seme",
              "n_ward": None,
              "c_doe": "11/04/2016",
              "n_doe": None,
              "c_dob": "19/02/2002",
              "n_dob": None,
              "AGYW_details": "1",
              "n_AGYW_details": None,
              "g_intervention": [
                {
                  "intervention_type": "1001",
                  "c_behavioural_1": "HCBF    2016-08-29",
                  "c_behavioural_2": "SHUGA II.   2020-06-14",
                  "c_behavioural_3": "SHUGA II.   2020-06-14",
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": "1002",
                  "biomedical": None,
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "1",
                  "external_organization_interventions": "2",
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "1001",
                  "c_behavioural_1": "HCBF    2016-08-29",
                  "c_behavioural_2": "SHUGA II.   2020-06-14",
                  "c_behavioural_3": "SHUGA II.   2020-06-14",
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": "1008",
                  "biomedical": None,
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "1",
                  "external_organization_interventions": "4",
                  "other_external_organization_interventions": "Test",
                  "other_intervention_types": "Test",
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "2001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": "HTS (Client) 2017-05-20",
                  "c_biomedical_2": "HTS (Client) 2019-11-21",
                  "c_biomedical_3": "HTS (Client) 2019-11-21",
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": "2002",
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "1",
                  "external_organization_interventions": "2",
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": "201",
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "2001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": "HTS (Client) 2017-05-20",
                  "c_biomedical_2": "HTS (Client) 2019-11-21",
                  "c_biomedical_3": "HTS (Client) 2019-11-21",
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": "2003",
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "1",
                  "external_organization_interventions": "2",
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": "Test",
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "2001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": "HTS (Client) 2017-05-20",
                  "c_biomedical_2": "HTS (Client) 2019-11-21",
                  "c_biomedical_3": "HTS (Client) 2019-11-21",
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": "2006",
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "2",
                  "external_organization_interventions": None,
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": "12345",
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "2001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": "HTS (Client) 2017-05-20",
                  "c_biomedical_2": "HTS (Client) 2019-11-21",
                  "c_biomedical_3": "HTS (Client) 2019-11-21",
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": "2007",
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "2",
                  "external_organization_interventions": None,
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": "101",
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "2001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": "HTS (Client) 2017-05-20",
                  "c_biomedical_2": "HTS (Client) 2019-11-21",
                  "c_biomedical_3": "HTS (Client) 2019-11-21",
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": "2037",
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "2",
                  "external_organization_interventions": None,
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": "Test",
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "3001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": "Physical Violence - PSS 2019-01-16",
                  "c_post_gbv_2": "Physical Violence - Others (Specify) 2019-01-16",
                  "c_post_gbv_3": "Physical Violence - Others (Specify) 2019-01-16",
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": None,
                  "post_gbv": "3010",
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "2",
                  "external_organization_interventions": None,
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "3001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": "Physical Violence - PSS 2019-01-16",
                  "c_post_gbv_2": "Physical Violence - Others (Specify) 2019-01-16",
                  "c_post_gbv_3": "Physical Violence - Others (Specify) 2019-01-16",
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": None,
                  "post_gbv": "3024",
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "1",
                  "external_organization_interventions": "1",
                  "other_external_organization_interventions": None,
                  "other_intervention_types": "Test",
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "3001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": "Physical Violence - PSS 2019-01-16",
                  "c_post_gbv_2": "Physical Violence - Others (Specify) 2019-01-16",
                  "c_post_gbv_3": "Physical Violence - Others (Specify) 2019-01-16",
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": None,
                  "post_gbv": "3025",
                  "social_protection": None,
                  "other_interventions": None,
                  "external_organization": "2",
                  "external_organization_interventions": None,
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": "Test",
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "4001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": "Economic Strengthening - Financial Capabilities Training 2017-01-17",
                  "c_social_protection_2": "Economic Strengthening - Entrepreneurship training 2020-05-23",
                  "c_social_protection_3": "Physical Violence - Others (Specify) 2019-01-16",
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": None,
                  "post_gbv": None,
                  "social_protection": "4014",
                  "other_interventions": None,
                  "external_organization": "2",
                  "external_organization_interventions": None,
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "4001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": "Economic Strengthening - Financial Capabilities Training 2017-01-17",
                  "c_social_protection_2": "Economic Strengthening - Entrepreneurship training 2020-05-23",
                  "c_social_protection_3": "Physical Violence - Others (Specify) 2019-01-16",
                  "n_social_protection": None,
                  "c_other_intervention_1": None,
                  "c_other_intervention_2": None,
                  "c_other_intervention_3": None,
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": None,
                  "post_gbv": None,
                  "social_protection": "4007",
                  "other_interventions": None,
                  "external_organization": "1",
                  "external_organization_interventions": "5",
                  "other_external_organization_interventions": None,
                  "other_intervention_types": "Test",
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "5001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": "Social Asset Building - Number of Sessions Attended 2016-08-31",
                  "c_other_intervention_2": "Social Asset Building - Number of Sessions Attended 2017-07-30",
                  "c_other_intervention_3": "Social Asset Building - Number of Sessions Attended 2020-06-14",
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": None,
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": "5006",
                  "external_organization": "2",
                  "external_organization_interventions": None,
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                },
                {
                  "intervention_type": "5001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": "Social Asset Building - Number of Sessions Attended 2016-08-31",
                  "c_other_intervention_2": "Social Asset Building - Number of Sessions Attended 2017-07-30",
                  "c_other_intervention_3": "Social Asset Building - Number of Sessions Attended 2020-06-14",
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": None,
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": "5008",
                  "external_organization": "1",
                  "external_organization_interventions": "3",
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": None,
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": 10,
                  "comments": None
                },
                {
                  "intervention_type": "5001",
                  "c_behavioural_1": None,
                  "c_behavioural_2": None,
                  "c_behavioural_3": None,
                  "n_behavioural": None,
                  "c_biomedical_1": None,
                  "c_biomedical_2": None,
                  "c_biomedical_3": None,
                  "n_biomedical": None,
                  "c_post_gbv_1": None,
                  "c_post_gbv_2": None,
                  "c_post_gbv_3": None,
                  "n_post_gbv": None,
                  "c_social_protection_1": None,
                  "c_social_protection_2": None,
                  "c_social_protection_3": None,
                  "n_social_protection": None,
                  "c_other_intervention_1": "Social Asset Building - Number of Sessions Attended 2016-08-31",
                  "c_other_intervention_2": "Social Asset Building - Number of Sessions Attended 2017-07-30",
                  "c_other_intervention_3": "Social Asset Building - Number of Sessions Attended 2020-06-14",
                  "n_other": None,
                  "behavioural": None,
                  "biomedical": None,
                  "post_gbv": None,
                  "social_protection": None,
                  "other_interventions": "5010",
                  "external_organization": "2",
                  "external_organization_interventions": None,
                  "other_external_organization_interventions": None,
                  "other_intervention_types": None,
                  "referral": "Test",
                  "intervention_date": "2020-10-16",
                  "c_intervention_date": "16/10/20",
                  "hts_results": None,
                  "client_ccc_number": None,
                  "pregnancy_test_reults": None,
                  "number_of_sessions_attended": None,
                  "comments": None
                }
              ],
              "comment_additional_services": None,
              "person_updating": "James",
              "date_updated": "2020-10-16",
              "c_date_updated": "16/10/20",
              "comments_notes": None,
              "instanceID": "uuid:9bca070c-9a48-4359-90c5-0642b5e1de05",
              "instanceName": "DREAMS INTERVENTION 5 5/1204/17 James"
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
        self.assertEqual(15, len(converted_json))

        for intervention in converted_json:
            self.assertEqual(intervention["client"], "1")
            self.assertEqual(intervention["dreams_id"], "5/1204/17")

        intervention_date_for_the_first_intervention = converted_json[0]["intervention_date"]
        self.assertEqual(intervention_date_for_the_first_intervention, "2020-10-16")

    def test_get_value_or_none_returns_none(self):
        converted_json = json.loads("{ \"key\": null  }")
        returned_value = DreamsInterventionMediator.get_value_or_none(converted_json, "key")
        self.assertIsNone(returned_value)

    def test_get_value_or_none_returns_value(self):
        converted_json = json.loads("{ \"key\": 4  }")
        returned_value = DreamsInterventionMediator.get_value_or_none(converted_json, "key")
        self.assertEqual(4, returned_value)

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
