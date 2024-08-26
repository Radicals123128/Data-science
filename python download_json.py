import requests

url = 'https://api.github.com/users/hadley/orgs'   
response = requests.get(url)
with open('file.json', 'wb') as file:
    file.write(response.content)
