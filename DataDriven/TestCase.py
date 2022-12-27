import json
import jsonpath
import requests
import openpyxl
from DataDriven import Library

def test_DataDriven():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    open_file = open("C:/Users/91994/Desktop/Python_API_Data/Read_JsonFile.json")
    json_requests = json.loads(open_file.read())

# Creating Object for Library file and importing the class
    obj = Library.Common("C:/Users/91994/Desktop/Python_API_Data/excel_data.xlsx", "Sheet1")
    row_count = obj.fetch_row_count()
    print(f"Row Count : {row_count}")
    col_count = obj.fetch_column_count()
    print(f"Column Count : {col_count}")
    key_names = obj.fetch_key_names()
    print(f"Key Names : {key_names}")

    for i in range(2,row_count+1):
        updated_json_request = obj.update_requests_with_data(i,json_requests,key_names)
        response = requests.post(API_URL,updated_json_request)
        print(response.text)
        print(response.status_code)


