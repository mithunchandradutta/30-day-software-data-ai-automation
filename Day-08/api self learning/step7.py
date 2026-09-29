import requests

url = "https://jsonplaceholder.typicode.com/users/9999"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.ConnectionError:
    print("No Internet")
except requests.exceptions.Timeout:
    Print("অনেক দেরি হচ্ছে")