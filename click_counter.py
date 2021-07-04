import os
import requests
from dotenv import load_dotenv


def check_link(link, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    header = {'Authorization': f'{token}'}
    response = requests.get(url, headers=header)
    return response.ok


def remake_checked_link(checked_link):
    count_clicks(link, token) if checked_link else shorten_link(link, token)


def shorten_link(link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {'Authorization': f'{token}'}
    payload = {'long_url': f'{link}'}
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()
    bitlink = response.json()['link']
    print('Битссылка', bitlink)


def count_clicks(link, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
        'unit': 'day',
        'units': -1
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    print('Кликов:', clicks_count)


def check_link_data(checked_link):
    try:
        remake_checked_link(checked_link)
    except requests.exceptions.HTTPError:
        print('Вы ввели неверную ссылку')


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    link = input('Введите URL: ')
    checked_link = check_link(link, token)
    check_link_data(checked_link)