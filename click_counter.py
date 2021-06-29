import requests


header = {'Authorization': 'Bearer 4b7bfd41c0bd5262c762e6b209dbd9b2b170fa1f'}
url = 'https://api-ssl.bitly.com/v4/user'
response = requests.get(url, headers=header)
response.raise_for_status()
print(response.text)