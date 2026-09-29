import requests

params = {"userId": 2}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

print(response.url)
posts = response.json()
print(len(posts))

for post in posts:
    print(post["title"])
