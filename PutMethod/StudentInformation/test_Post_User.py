import requests
import json
import jsonpath

def test_add_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    Open_File = open("C:/Users/91994/Desktop/Python_API_Data/NewStudentDetails.json",'r')
    json_request = json.loads(Open_File.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

# def test_get_student_data():
#     API_URL = "http://thetestingworldapi.com/api/studentsDetails/544086"
#     response = requests.get(API_URL)
#     print(response.text)
#
# def test_validate_student_data():
#     API_URL = "http://thetestingworldapi.com/api/studentsDetails/544086"
#     response = requests.get(API_URL)
# # we can use the below 2 ways to convert the data to json
#     # json_response = json.loads(response.text)
#     json_response = response.json()
#     validate_id = jsonpath.jsonpath(json_response,"data.id")
#     assert validate_id[0] == 544086

def test_update_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/544116"
    open_file = open("C:/Users/91994/Desktop/Python_API_Data/NewStudentDetails.json",'r')
    json_request = json.loads(open_file.read())
    response = requests.put(API_URL,json_request)
    print(response.text)

# def test_get_updated_data():
#     API_URL = "http://thetestingworldapi.com/api/studentsDetails/544086"
#     response = requests.get(API_URL)
#     json_response = response.json()
#     middle_name_value = jsonpath.jsonpath(json_response,"data.middle_name")
#     print(middle_name_value)
#     assert middle_name_value[0] == 'Venugopal'

def test_delete_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/544116"
    response = requests.delete(API_URL)
    print(response.text)

def test_get_delete_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/544116"
    response = requests.get(API_URL)
    json_file = response.json()
    value_deleted = jsonpath.jsonpath(json_file,"data.id")
    print(value_deleted)
    # assert value_deleted[0] != 544086