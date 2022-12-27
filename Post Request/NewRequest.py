import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

# Create file and Read File
file_open = open("C:\\Users\\91994\\PycharmProjects\\RestAPI\\APIBasic-Pytest\\TestData\\NewUser.json",'r')
file_read = file_open.read()

# Parse file to Json Formatt
json_file = json.loads(file_read)

# Post the File using Post Method
json_response = requests.post(url,json_file)
print(json_response.content)
assert json_response.status_code == 201

# parse into json formatt text
json_text = json.loads(json_response.text)

# fetch values using key in jsonpath
jsonpath_fetch = jsonpath.jsonpath(json_text,'name')
print(jsonpath_fetch[0])

