import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint


HOST = 'https://minfin.com.ua/'
URL = 'https://minfin.com.ua/cards/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):

    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='be80pr-1 gdrIQA')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='be80pr-15 kwXsZB').find('a', class_='cpshbz-0 eRamNS').get('alt'),
                'link_product': item.find('div', class_='be80pr-15 kwXsZB').find('a').get('href'),
                'bank': item.find('div', class_='be80pr-16 be80pr-17 kpDSWu cxzlon').find('a', class_='be80pr-35 UOQtz').get('alt'),
            }
        )
    return cards


html = get_html(URL)
pprint(get_content(html.text))


