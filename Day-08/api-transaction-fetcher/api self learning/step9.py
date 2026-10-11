import requests

headers = {
    "User-Agent": "mithun-learning-script",
    "X-My-Name": "Mithun"  
}

response = requests.get("https://httpbin.org/headers", headers=headers)
print(response.json())