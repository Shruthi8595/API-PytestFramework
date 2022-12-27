import requests
import json
import jsonpath

def test_add_student_data():
    # Add New Student details
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    open_file = open("C:\\Users\\91994\\PycharmProjects\\RestAPI\\APIBasic-Pytest\\TestData\\NewStudentDetails.json",'r')
    json_format = json.loads(open_file.read())
    json_response = requests.post(API_URL,json_format)
    fetch_id = jsonpath.jsonpath(json_response.json(),'id')
    print(f"Student Details : {fetch_id[0]}")

    # Add Student Technical Skills
    TechSkills_URL = "http://thetestingworldapi.com/api/technicalskills"
    open_techfile = open("C:\\Users\\91994\\PycharmProjects\\RestAPI\\APIBasic-Pytest\\TestData\\StudentTechnicalSkills.json",'r')
    json_techfile = json.loads(open_techfile.read())
    json_techfile['id'] = int(fetch_id[0])
    json_techfile['st_id'] = fetch_id[0]
    techfile_response = requests.post(TechSkills_URL,json_techfile)
    print(f"Technical Details : {json_techfile}")
    print(techfile_response.text)

    # Add Student Address
    Address_URL = "http://thetestingworldapi.com/api/addresses"
    open_addressfile = open("C:\\Users\\91994\\PycharmProjects\\RestAPI\\APIBasic-Pytest\\TestData\\StudentAddressDetails.json")
    json_addressfile = json.loads(open_addressfile.read())
    json_addressfile['stId'] = fetch_id[0]
    print(f"Addressfile Details : {json_addressfile}")
    addressfile_response = requests.post(Address_URL, json_addressfile)
    print(addressfile_response.text)

    # Final Student details
    Finalsetails_URL = "http://thetestingworldapi.com/api/FinalStudentDetails/"+str(fetch_id[0])
    final_response = requests.get(Finalsetails_URL)
    print(final_response.text)

