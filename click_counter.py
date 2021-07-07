import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def remake_http_url(link, token):
    parted_url = urlparse(link)
    checking_link = f'{parted_url.netloc}{parted_url.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{checking_link}'
    header = {'Authorization': token}
    response = requests.get(url, headers=header)
    return checking_link if response.ok else link


def check_bitlink(checked_link, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{checked_link}'
    header = {'Authorization': token}
    response = requests.get(url, headers=header)
    return response.ok


def shorten_link(checked_link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {'Authorization': token}
    payload = {'long_url': checked_link}
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(checked_link, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{checked_link}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
        'unit': 'day',
        'units': -1
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    link = input('Введите URL: ')
    checked_link = remake_http_url(link, token)
    server_response = check_bitlink(checked_link, token)
    try:
        if server_response:
            print('Кликов:', count_clicks(checked_link, token))
        else:
            print('Битссылка:', shorten_link(checked_link, token))
    except requests.exceptions.HTTPError:
        print('Вы ввели неверную ссылку')
