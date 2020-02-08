import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import Movie, Actor


class BaseTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.executive_producer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1URkNSRGMyUWpsRVFqTTNRamhCTUVJNE9EQkJOVGN6UkRZMk5qVkZOVVE1UlRJNU56UkNSUSJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AwMS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWUxNzY4ZjE1MDgxNDUwZThkYTVmMDlmIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNTgxMTQ0NTk5LCJleHAiOjE1ODExODA5OTksImF6cCI6ImpJR1liYkJmOFlzREhZMFV2QXlQNHNaMkY3RTlBNkRUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOmRyaW5rcyIsImdldDphY3RvcnMiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDpkcmlua3MiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6ZHJpbmtzIl19.FeZxX_a2ZDHCxW-psY1t9_dxw-ZNYfcURT0Xq9Wzr_Wgul96Ezfl7fwQWHn9kcgxMMyEReB7_gXIG-5HnuNemfTwwzhsp-jFQplVki9BivFtq6PK1br6GljuzsGulqPOZ3QeXdUN9BBPrePaLBsUnNpf2r-fGNYyUyL7BkFpgOwPU5kSTDAWyAAtmfWQqRgHvgydf-0Cq9DDYodsJQDIGtpc6SBHPwqzDCGT7OiDFassbeDycfSMCbjGdCMTKQs_rdX29P60bVx-89L6Xn2YyiChLtDqygvhdaKwgfM_uX03fh5oZUNvUNMWVnWPo79M_8bTo20lLh9LAzzpioKz8A"

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_create_actors_with_executive_producer_token_success(self):
        data = {
            'name': 'test',
            'age': '30',
            'gender': 'female'
        }
        response = self.client().post(
            '/actors',
            json=data, headers={
                "Authorization":
                    "Bearer {}".format(self.executive_producer_token)
            })
        self.assertEqual(response.status_code, 201)

    def test_get_actors_success(self):

        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(self.executive_producer_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_get_movies_success(self):

        response = self.client().get(
            '/movies',
            headers={
                "Authorization":
                    "Bearer {}".format(self.executive_producer_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_get_actors_success(self):

        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(self.executive_producer_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
