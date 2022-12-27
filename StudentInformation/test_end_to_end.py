import os

import requests
import json
import jsonpath

def test_add_student_data():
    # Add New Student details
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"

    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    replace = ROOT_PATH.replace("StudentInformation", "TestData")
    myfile_path = os.path.join(replace, "NewStudentDetails.json")

    open_file = open(myfile_path,'r')
    json_format = json.loads(open_file.read())
    json_response = requests.post(API_URL,json_format)

    json_text = json.loads(json_response.text)
    fetchID = jsonpath.jsonpath(json_text,[0])
    print(fetchID)

    print(json_response.status_code)
    assert json_response.status_code == 200


    # # Add Student Technical Skills
    # TechSkills_URL = "http://thetestingworldapi.com/api/technicalskills"
    # open_techfile = open("C://Users//91994//Desktop//Python_API_Data//StudentTechnicalSkills.json",'r')
    # json_techfile = json.loads(open_techfile.read())
    # techfile_response = requests.post(TechSkills_URL,json_techfile)
    # print(techfile_response.text)
    #
    # # Add Student Address
    # Address_URL = "http://thetestingworldapi.com/api/addresses"
    # open_addressfile = open("C://Users//91994//Desktop//Python_API_Data//StudentAddressDetails.json")
    # json_addressfile = json.loads(open_addressfile.read())
    # addressfile_response = requests.post(Address_URL, json_addressfile)
    # print(addressfile_response.text)
    #
    # # Final Student details
    # Finaldetails_URL = "http://thetestingworldapi.com/api/FinalStudentDetails/544286"
    # final_response = requests.get(Finaldetails_URL)
    # print(final_response.text)

