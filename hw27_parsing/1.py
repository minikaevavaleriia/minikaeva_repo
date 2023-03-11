"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""

import re
import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def find_info(data):
    for i in data.find_all(re.compile("artist")):
        print(i.name)



def main():
    url = 'https://music.yandex.ru/chart'
    data = get_data(get_html(url))
    find_info(data)




main()