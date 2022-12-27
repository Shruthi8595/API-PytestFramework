import requests
# Url
url = "https://reqres.in/api/users/2"
response = requests.get(url)

print(f"Response Content : {response.content}")
print(f"Header Of the Response is : {response.headers}")
print(f"Response Status Code : {response.status_code}")

# Validate Response code
assert response.status_code == 200

# fetch date from header
print(f"Date in the response Header is : {response.headers.get('Date')}")

# fetch all the cookies
print(f"Cookies are : {response.cookies}")

# fetch Encoded data
print(f"Encoded Data : {response.encoding}")

# fetch Elapsed time : Time duration between Sending Reauests and Receiving the Response
print(f"Time duration between Sending Reauests and Receiving the Response : {response.elapsed}")