from django.test import TestCase
from django.test import Client
import json

# Create your tests here.
class UserTestCase(TestCase):


    def test_new_user_auth(self):
        request = {
            "clientId": "1194316053918870",
            "code": "CAACEdEose0cBAGhAZBEabCIQDkZAZCbyDA4sv5Wqbw7Qjxuok7IUZCI8MI5XbnZA4wiZBN03EVo8VZCzTAFdCZA9EDa3xIbQfZCRMrroQowbg1IiNvSURoRlxVIfR4pYM0nVhoOvtFIgX5otUeLeFrfCmZBV2RegselPkQS59Cj36fZC542KaTPJ0qjZBNwT8fWOmv3zQwk3jMKDH7WryND16MXZC",
            "redirectUri": "http://localhost:8000/",
        }
        client = Client()

        client.post('/api/auth/', content_type="application/json", data=json.dumps(request))
