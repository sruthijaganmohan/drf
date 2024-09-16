import requests

endpoint = "http://127.0.0.1:8000/api/products/8/update/"

data = {
    "title": "ketchup",
    "content": "condiment"
}

put_response = requests.put(endpoint, json=data)
print(put_response.json())