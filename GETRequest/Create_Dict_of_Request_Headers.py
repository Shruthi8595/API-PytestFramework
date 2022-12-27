import requests

# Sending Customised Header
headers_data = {'key1':'value1', 'key2':'value2'}
response = requests.get("https://httpbin.org/get",headers=headers_data)
print(response.text)