import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"
get_response = requests.get(url)
response_before_Updating = get_response.content
print(f"Getting Data before Updating : {response_before_Updating}")

# Create a Json file and read the file
file_open = open("C:\\Users\\91994\\PycharmProjects\\RestAPI\\APIBasic-Pytest\\TestData\\NewUser.json",'r')
file_read = file_open.read()

# parse the file into Json Format
json_file = json.loads(file_read)

#Put the Request and Get the Response
json_response = requests.put(url,json_file)
assert json_response.status_code == 200
print(f"Getting Data after updating:{json_response.content}")

# Parse json_response file into json format
json_text = json.loads(json_response.text)

jsonPath_Value = jsonpath.jsonpath(json_text,'job')
print(jsonPath_Value[0])


