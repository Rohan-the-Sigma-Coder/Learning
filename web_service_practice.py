import requests

headings = {
    "User-Agent": "my-python-script"
}
username = input('Enter username: ')
url = f'https://api.github.com/users/{username}'

response = requests.get(url, headers=headings)

if response.status_code == 200:
    data = response.json()
    
    print(f"Username: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Number of Followers: {data['followers']}")
else:
    print(f"Something went wrong: {response.status_code}")

