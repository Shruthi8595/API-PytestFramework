import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

# Parse Response to json
json_response = json.loads(response.text)
print(response.text)

# fetch value using JsonPath : gives result in list
length = len('data.first_name')
print(f"Lenth of the first Name : {length}")
for i in range (0,7):
    first_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    if isinstance(first_name,bool):
        print(f"Printing Is Instance : {first_name}")
    else:
        print(f"Inside For Loop : {first_name[0]}")