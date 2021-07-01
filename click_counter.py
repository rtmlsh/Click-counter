import requests
from dotenv import load_dotenv
load_dotenv()
TOKEN = '17c09e22ad155405159ca1977542fecf00231da7'
link = input('Введите URL: ')

def define_link(link=link, token = TOKEN):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'f'{link}'
    header = {'Authorization': f'{token}'}
    response = requests.get(url, headers=header)
    check_clicks_count() if response else check_short_link()

def shorten_link(token=TOKEN, link=link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {'Authorization': f'{token}'}
    payload = {'long_url': f'{link}'}
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()
    return (response.json()['link'])

def check_short_link():
    try:
        bitlink = shorten_link()
        print('Битссылка:', bitlink)
    except requests.exceptions.HTTPError:
        print('Вы ввели неверную ссылку 1')

def count_clicks(link=link, token=TOKEN):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'f'{link}''/clicks/summary'
    headers = {'Authorization': 'Bearer 'f'{token}'}
    payload = {
        'unit': 'month',
        'units': -1
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']

def check_clicks_count():
    try:
        clicks_count = count_clicks()
        print('Кликов:', clicks_count)
    except requests.exceptions.HTTPError:
        print('Вы ввели неверную ссылку 2')

# https://bit.ly/2GE4ZC3
# https://yandex.ru/

define_link()




