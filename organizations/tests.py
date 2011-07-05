import unittest
from django.test.client import Client
from noi_test.organizations.models import Organization

class OrganizationTestCase(unittest.TestCase):
    def setUp(self):
        self.naacp = Organization.objects.create(name="NAACP",founded_date="1945-12-22", legal_status="5013c", number_staff="12")
        self.naacp.person_set.create(name='Michael Jordan', email="mj@nba.com", phone="1234567", attended_trainings="N", electoral_experience="Y", active_projects="none")
        self.naacp.internal_set.create(relationship_status="Ma", familiarity="Y", action_steps="None", activity_level="Pr")
        
    def test_orgs(self):
        "This test should pass. Testing creation of organizations and person."
        self.assertEqual(self.naacp.number_staff,'12')
        self.assertEqual(self.naacp.person_set.all().count(), 1)
    
    def test_internal(self):
        "This test should fail. We cannot add more than one internal per organization."
        self.naacp.internal_set.create(relationship_status="Di", familiarity="N", action_steps="None", activity_level="Re")
        