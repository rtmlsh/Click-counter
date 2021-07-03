import os
import requests
from dotenv import load_dotenv


def define_link(link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'f'{link}'
    header = {'Authorization': f'{token}'}
    response = requests.get(url, headers=header)
    check_clicks_count() if response else check_short_link()


def shorten_link(link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {'Authorization': f'{token}'}
    payload = {'long_url': f'{link}'}
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()
    return (response.json()['link'])


def count_clicks(link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'f'{link}''/clicks/summary'
    headers = {'Authorization': 'Bearer 'f'{token}'}
    payload = {
        'unit': 'day',
        'units': -1
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']


def check_short_link():
    try:
        bitlink = shorten_link(link=link, token=token)
        print('Битссылка:', bitlink)
    except requests.exceptions.HTTPError:
        print('Вы ввели неверную ссылку')


def check_clicks_count():
    try:
        clicks_count = count_clicks(link=link, token=token)
        print('Кликов:', clicks_count)
    except requests.exceptions.HTTPError:
        print('Вы ввели неверную ссылку')


def main():
    define_link(link, token)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TOKEN')
    link = input('Введите URL: ')
    main()