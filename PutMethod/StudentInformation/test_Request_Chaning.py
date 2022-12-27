"""
Request Chaining : Whatever the data we are fetching we are passing into another requests is Request Chaining
"""

import requests
import json
import jsonpath

def test_add_new_student():
    global json_response
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    open_file = open("C:/Users/91994/Desktop/Python_API_Data/NewStudentDetails.json", 'r')
    json_file = json.loads(open_file.read())
    response = requests.post(API_URL,json_file)
    json_response = jsonpath.jsonpath(response.json(),'id')
    print(json_response[0])

def test_get_details():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/"+str(json_response[0])
    response = requests.get(API_URL)
    print(response.text)
    # print(response.content)
    # print(response.headers)