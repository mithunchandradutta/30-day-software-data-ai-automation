import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

print(type(users))
print(len(users))

for user in users:
    print(user["id"], user["name"])