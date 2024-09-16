import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {"title": "ketchup", "content": "condiment", "price": 5.99}

post_response = requests.post(endpoint, json=data)
print(post_response.json())