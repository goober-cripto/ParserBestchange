from BestParser import BestParser


if __name__ == "__main__":
    try:
        url = 'https://www.bestchange.net/wiki/rates.html'
        parser = BestParser(url)
        html_content = parser.fetch_html_content()
        currencies = parser.parse_currencies(html_content)

        print("Тикеры валют:")
        print(currencies)

    except Exception as e:
        print(e)
