import requests


TOKEN = '17c09e22ad155405159ca1977542fecf00231da7'
link = input('Введите URL для сокращения: ')
short_link = input('Введите битлинк: ')

def shorten_link(token=TOKEN, link=link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {'Authorization': f'{token}'}
    payload = {'long_url': f'{link}'}
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()
    return (response.json()['link'])

try:
    bitlink = shorten_link()
    print('Битссылка:', bitlink)
except requests.exceptions.HTTPError:
    print('Вы ввели неверную ссылку')

def count_clicks(bitlink=short_link, token=TOKEN):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'f'{bitlink}''/clicks/summary'
    headers = {'Authorization': 'Bearer 'f'{token}'}
    payload = {
        'unit': 'month',
        'units': -1
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']

try:
    clicks_count = count_clicks()
    print('Кликов:', clicks_count)
except requests.exceptions.HTTPError:
    print('Вы ввели неверную ссылку')

# https://bit.ly/2GE4ZC3
# https://yandex.ru/






