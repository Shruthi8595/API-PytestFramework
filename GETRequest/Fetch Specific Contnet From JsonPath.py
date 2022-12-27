import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

# Parse Response to json
json_response = json.loads(response.text)
print(json_response)

# fetch value using JsonPath : gives result in list
first_name = jsonpath.jsonpath(json_response,'data[0].first_name')
print(first_name[0])

first_name = jsonpath.jsonpath(json_response,'data[2].first_name')
print(first_name[0])

