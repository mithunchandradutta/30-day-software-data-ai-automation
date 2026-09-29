import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"

try: 
    response = requests.get(url, timeout = 10)
    response.raise_for_status()
    users = response.json()
except requests.exceptions.RequestException as e:
    print("Error:", e)
    raise SystemExit
rows = []
for U in users:
    rows.append({
        "id": U["id"],
        "name": U["name"],
        "email": U["email"],
        "city": U["address"]["city"],
    })


with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "email", "city"])
    writer.writeheader()
    writer.writerows(rows)


print(len(rows), "জন user users.csv তে save হয়েছে")