import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

data = response.json ()
print(data)
print(type(data))

print(data["name"])
print(data["email"])
print(data["address"] ["city"])