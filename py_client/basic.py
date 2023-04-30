import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={"product_id": 123}, json={})
# print(get_response.text) # raw text/html
print(get_response.json())