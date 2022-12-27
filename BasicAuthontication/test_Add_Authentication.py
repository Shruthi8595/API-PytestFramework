"""
Authentication : Some of the API's are not available directly so we need to send username and password
with requests so server will identify user according to that it will send response this we call it as Authentication
Here we send requests with authentication
"""
import requests
from requests.auth import HTTPBasicAuth


def test_basic_auth():
    api_url = "https://api.github.com/user"
    response = requests.get(api_url,auth=HTTPBasicAuth('Shruthi8595','shru8595'))
    print(response.text)