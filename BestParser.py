import requests
from bs4 import BeautifulSoup
from typing import List


class BestParser:

    def __init__(self, url):
        """
        Парсер сайта www.bestchange.net
        """
        self.url = url

    def fetch_html_content(self):
        """
        Выполняет HTTP-запрос к указанному URL
        и возвращает полученный HTML-код в виде строки.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None

    def parse_currencies(self, html_content) -> List[str]:
        """
        Предназначена для парсинга HTML-кода веб-страницы, извлечения информации
        о валютных тикерах и сохранения их в список.
        """
        soup = BeautifulSoup(html_content, 'lxml')
        table = soup.find('h2', string='Коды электронных валют').find_next('table')
        tickers: List[str] = []
        for row in table.find_all('tr')[1:]:
            # Извлекаем текст из ячейки таблицы и добавляем его в список
            ticker = row.find('td', class_="oddleft").text.strip()
            tickers.append(ticker)

        return tickers

    def combine_with_each(self, items: List[str]) -> List[str]:
        """
        Принимает список элементов и для каждого элемента этого списка
        добавляет другой элемент из списка тикеров, за исключением текущего элемента.
        Пример: BTCETH, BTCRUB
        """
        combined_list: List[str] = []
        for item in items:
            for ticker in items:
                if ticker != item:
                    combined_list.append(f"{item}{ticker}")
        return combined_list
