import json
from django.test import TestCase

from mediators.dreams_intervention_mediator import DreamsInterventionMediator


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

    def test_convert_to_dream_intervention_api_json_returns_correct_data(self):
        mediator = DreamsInterventionMediator()
        converted_json_str = mediator.convert_to_dream_intervention_api_json(self.odk_json)
        self.assertIsNotNone(converted_json_str)

        converted_json = json.loads(converted_json_str)
        self.assertEqual(15, len(converted_json))

        for intervention in converted_json:
            self.assertEqual(intervention["client_id"], "1")
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
