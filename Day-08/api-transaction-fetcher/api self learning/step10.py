import requests

url = "https://httpbin.org/bearer"

# without token
r1 = requests.get(url)
print("Without token", r1.status_code)

# with token
headers = {"Authorization": "Bearer my-secret-token"}
r2 = requests.get(url, headers=headers)
print("With TOken", r2.status_code)
print(r2.json())
