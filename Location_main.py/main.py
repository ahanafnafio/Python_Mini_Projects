import requests

response = requests.get("https://ipinfo.io/json").json()

print(f"city: {response['city']}")
print(f"region: {response['region']}")
print(f"country: {response['country']}")