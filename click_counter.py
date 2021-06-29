import requests

header = {'Authorization': '17c09e22ad155405159ca1977542fecf00231da7'}
payload = {'long_url': 'https://yandex.ru/'}
url = 'https://api-ssl.bitly.com/v4/bitlinks'
response = requests.post(url, headers=header, json=payload)
response.raise_for_status()
print(response.text)
