import os
import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser(description='Скрипт позволяет получить битлинк из ссылки и посчитать количество кликов по ней')
    parser.add_argument('link', help='Передайте битлинк или ссылку в качестве аргумента при запуске скрипта')
    return parser


def crop_url(link):
    parted_url = urlparse(link)
    checking_link = f'{parted_url.netloc}{parted_url.path}'
    return checking_link


def check_bitlink(cropped_link, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{cropped_link}'
    header = {'Authorization': token}
    response = requests.get(url, headers=header)
    return response.ok


def shorten_link(link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {'Authorization': token}
    payload = {'long_url': link}
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(cropped_link, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{cropped_link}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
        'unit': 'day',
        'units': -1
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    link = args.link
    cropped_link = crop_url(link)
    server_response = check_bitlink(cropped_link, token)
    try:
        if server_response:
            print('Кликов:', count_clicks(cropped_link, token))
        else:
            print('Битссылка:', shorten_link(link, token))
    except requests.exceptions.HTTPError:
        print('Вы ввели неверную ссылку')
