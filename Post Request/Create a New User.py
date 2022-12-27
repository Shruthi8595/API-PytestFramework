"""
Post Method is used to Create a New Record
"""
import jsonpath
import requests
import json

url = "https://reqres.in/api/users"

# Create Json file and read the file
file = open("C:\\Users\\91994\\PycharmProjects\\RestAPI\\APIBasic-Pytest\\TestData\\NewUser.json",'r')
file_input = file.read()
json_file = json.loads(file_input)

# Make a Post Request with Json Input body
json_post = requests.post(url,json_file)
print(json_post.content)
assert json_post.status_code == 201

# fetch header from response
print(json_post.headers)
print(json_post.headers.get('Content-Length'))

# parse response to json format
response_json = json.loads(json_post.text)

# Pick the value using Jsonpath
Id_value = jsonpath.jsonpath(response_json,'id')
print(Id_value[0])


