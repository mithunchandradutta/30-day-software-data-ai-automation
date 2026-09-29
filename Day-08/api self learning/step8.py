import requests

new_post = {
    "title": "Day 8",
    "body": "I'am Learning API",
    "userId": 1
}

response =  requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

print(response.status_code)
print(response.json())