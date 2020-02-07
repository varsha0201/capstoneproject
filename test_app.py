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
        self.executive_producer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFqbEdORGRETVRoQk1FWXhOVEJFUVRBNU9FSkVOa0kxTkRrMFJFRTJRVFJHUlVFNU9VRTJOUSJ9.eyJpc3MiOiJodHRwczovL2VsbGllc2VycnkuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2MjkzOTU0MDU5NzkxNzYzODM1IiwiYXVkIjpbImNvZmZlZXNob3AiLCJodHRwczovL2VsbGllc2VycnkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4MDc1NTk2NiwiZXhwIjoxNTgwODQyMzY2LCJhenAiOiJiOFEzNDE4SU9WN1hoZHlVcjBaaGZ4UmYxcFgzUVoycyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.UNbqpauah9QP1prd5svaPSn1kxrcvehcEGEpNvxBWc-y5iUhwX33JupLpNGaRsdsvL0W6xHizrddY6By3eUQHnBPOX1MbIR-vnR5pyYBtrxWlNKSSgeQo2a3wZBZjKglOcWNeVWaLQM2hT27rLjZ-NfWHwngvWGuNIHo_wISn3lsbId8Ss3QPV7h1kRJwDsDK74_3ybfmmh3c3EDbvQlQpdG6V2zi2FYizgSd84Z6XhMc8_3zQsRP0ewm8weYuAcOdRdtBfU8tMJ2LF2mxwkIGnQtNlAOiMrDGXtcLr8eM7a3RtVIPxzyPvj21nsjYBLAlm_h7U1ZTXqan3hPDjIWQ"
        
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
