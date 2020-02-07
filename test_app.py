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
        self.executive_producer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1URkNSRGMyUWpsRVFqTTNRamhCTUVJNE9EQkJOVGN6UkRZMk5qVkZOVVE1UlRJNU56UkNSUSJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZXNob3AwMS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWUzZDZlN2M1MWYxMWUwZTdkZjg2NzRjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNTgxMDk0MjU2LCJleHAiOjE1ODExMDE0NTYsImF6cCI6ImpJR1liYkJmOFlzREhZMFV2QXlQNHNaMkY3RTlBNkRUIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.pxMwhcpu1GrQ2yaZ5JMPfDPvd4DW87gQwajzvcKzWJbxvMCjMY0HrtVMIyacn78j5tFIqfcvFbnGIDHda9uzTqUQH1LtOr4uAcWepaLeVjfQbA6ZjuzlPsqMscZFQJut6qUaK0xBHGmsxxcDQm_iuQ5hULSIJ3--QQKRKdqCdKj1NnXf_OsV80uPyu-ymVGgLJUrDuFZRX-iXp9FWgWSN7au6rYuwwxoKbBvtHX1Q-uuHiDv9WzAc1YoUWvR8fQxa8XBuNNFZppKtPKZPYn0rAZ2Rt4Fxj2ZxN44XYLBIB3IJhrbL_0cpr4bGr1tekOoi_19C7MvxDvWOt2WqnzWnw"
        
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
