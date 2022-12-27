"""
Parameters : Key and Value pair which places after ? is called Parameters
            They are Seperated with & ("url": "https://httpbin.org/get?name=Testing&number=571401&email=abc%40gmail.com")
            We Can send Parameters to the Server in 2 ways
                1. By Body : using Put and Post Requests
                2. By URL : using Parameters
            Procedure to send the Parameters to URL is:
                1. Create Dictionary of Parametes
                2. Send the Dictionary with requests Called Params
"""
import  requests

param = {'name':'Testing','number':'571401','email':'abc@gmail.com'}
response = requests.get("https://httpbin.org/get",params=param)
print(response.text)