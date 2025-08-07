import requests

urls = "https://wmomiti.com/" 
response = requests.get(urls)

print(f"Status Code {response.status_code}")

print("Response Body")
print(response.text)
