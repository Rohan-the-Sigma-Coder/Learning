import requests

response = requests.get('http://192.168.86.24:8080/api/hello')
print(response.status_code)
print(response.json())
