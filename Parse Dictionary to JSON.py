"""
Serialization: converting an object into a JSON string.
Deserialization: converting a JSON string into an object.
"""""

# Parsing String to JSON format/Dict
import json
dic = '{"k1":"v1", "k2":"v2"}'
json_result = json.loads(dic)
print(json_result)

# Import the module
import json

# String with JSON format
data_JSON =  """
            {
                "size": "Medium",
                "price": 15.67,
                "toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
                "client": {
                    "name": "Jane Doe",
                    "phone": "455-344-234",
                    "email": "janedoe@email.com"
                }
            }
"""

# Convert JSON string to dictionary
data_dict = json.loads(data_JSON)
print(data_dict)

# JSON format with String
data_JSON =  {
                "name": "Nora",
                "age": 56,
                "id": "45355",
                "eye_color": "green",
                "wears_glasses": False
            }


# Convert dictionary to JSON string
data_dict = json.dumps(data_JSON)
print(data_dict)
