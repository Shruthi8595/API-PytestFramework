"""
GrantType = How my server is giving access
JWT stands for JSON Web Token
JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for
securely transmitting information between parties as a JSON object.
This information can be verified and trusted because it is digitally signed.
"""

import json
from idlelib.iomenu import encoding

import requests
import jsonpath
from collections.abc import Mapping

def test_oauth_token():
# token url
    token_url = "http://thetestingworldapi.com/Token"
# passing the data through url, this data will be provided
    data = {'grant_type':'password', 'username':'admin','password':'adminpass'}
# Fetching the access_token value by sending token url and data
    response = requests.post(token_url,data)
    print(response.text)
# converting the response to json format and fetching access token value
    token_value = jsonpath.jsonpath(response.json(),'access_token')
# creating an dictorinary and storing to Authorization key
    auth = {'Authorization':'Bearer '+token_value[0]}
    print(auth)

# Now sending the request using authorization and getting response
    API_URL = "http://thetestingworldapi.com/api/StDetails/544286"
    response = requests.get(API_URL,headers=auth)
    print(response)
    print(response.text)

# 1WS project
def JWT_Token(Username:str, env:str):
    token_url = "https:www.testingWorld." + env + " .com"
# If we have dirrent Env and Username
    file = open("file location" + env + "filepath.json", 'r')
    read_file = file.read()
    load_file = json.loads(read_file)
    print(load_file[0][Username])

    data = {'username': load_file[0][Username]}
    response = requests.get(token_url, headers=data)
    auth_token = str(response.content, encoding)
    JWTToken = 'Barrer' + auth_token
    print(JWTToken)


