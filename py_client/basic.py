import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title": "Chips", "content": "snacks", "price": 4.50})
print(get_response.json())