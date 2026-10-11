import requests

r1 = requests.get("https://jsonplaceholder.typicode.com/users/1")
r2 = requests.get("https://jsonplaceholder.typicode.com/users/9999")


print(r1.status_code)
print(r2.status_code)
