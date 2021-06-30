import requests


TOKEN = '17c09e22ad155405159ca1977542fecf00231da7'
url = 'https://api-ssl.bitly.com/v4/bitlinks'
link = input('Введите URL для сокращения: ')

def shorten_link(url=url, token=TOKEN, link=link):
    header = {'Authorization': f'{token}'}
    payload = {'long_url': f'{link}'}
    response = requests.post(f'{url}', headers=header, json=payload)
    response.raise_for_status()
    return (response.json()['link'])

#обернуть в main
try:
    bitlink = shorten_link()
    print('Битссылка', bitlink)
except requests.exceptions.HTTPError:
    print('Вы ввели неверную ссылку')







