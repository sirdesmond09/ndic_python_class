import requests

base_url = "http://127.0.0.1:8000/v1"


payload = {
    "name" : "Furniture",
    "desc" : "This contains all household and office furniture."
}

# response = requests.get(url = f"{base_url}/categories")

response = requests.post(url = f"{base_url}/categories/", data = payload)


print(response.status_code)
print(response.json())

