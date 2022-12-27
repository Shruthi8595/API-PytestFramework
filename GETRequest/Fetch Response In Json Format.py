import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

# Parse Response to json
json_response = json.loads(response.text)
print(json_response)

# fetch value using JsonPath : gives result in list
jsonpath_response = jsonpath.jsonpath(json_response,'total_pages')
print(jsonpath_response)
print(jsonpath_response[0])
assert jsonpath_response[0] == 2