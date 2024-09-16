import requests

product_id = input("Enter the product-id you want to delete:\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"
    delete_respone = requests.delete(endpoint)
    print(delete_respone.status_code==204)
