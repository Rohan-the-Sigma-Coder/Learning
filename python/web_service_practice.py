import requests

def git_webservice_practice():
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




def post_practice():
    url = 'https://jsonplaceholder.typicode.com/posts'
    title = input('Enter blog post title: ')
    body = input('Enter blog post body: ')
    data = {
        'title': title,
        'body': body,
        'userId': 1
    }
    response = requests.post(url, json = data)
    
    print(f"Status code: {response.status_code}")
    print(f"Response JSON: {response.json()}")



def put_practice():
    post_id = input('Post id: ')
    new_title = input('New title: ')
    new_body = input('New body: ')
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    updated_data = {
        'title': new_title,
        'body': new_body,
        'userId': 1
    }
    response = requests.put(url, json=updated_data)

    print(f'Status Code: {response.status_code}')
    print(f'Response JSON: {response.json()}')




def delete_practice():
    post_id = input('Enter post id: ')
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.delete(url)

    if response.status_code in (200, 204):
        print(f'Successfully deleted the content, status Code: {response.status_code}')
    else:
        print(f'Something went wrong: {response.status_code}')






