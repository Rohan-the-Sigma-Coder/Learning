import requests

response = requests.get('http://127.0.0.1:5000/hello/square/4')
print(response.status_code)
print(response)
