import requests
import matplotlib.pyplot as plt
import numpy as np

language_list = []
bytes_list = []

user_name = input('Enter username: ')
repos_url = f'https://api.github.com/users/{user_name}/repos'


response = requests.get(repos_url)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        repo_name = repo['name']
        languages_url = repo['languages_url']
        lang_response = requests.get(languages_url)

        if lang_response.status_code == 200:
            languages = lang_response.json()
            print(f"Repository: {repo_name}")
            for lang, bytes_of_code in languages.items():
                print(f"{lang}: {bytes_of_code} bytes")
                language_list.append(lang)
                bytes_list.append(bytes_of_code)
            pie_chart_array = np.array(bytes_list)
            plt.pie(pie_chart_array, labels = language_list)
            plt.show()
        else:
            print(f"Failed to get languages for repo {repo_name}")
else:
    print(f'Failed to fetch repositories: {response.status_code}')