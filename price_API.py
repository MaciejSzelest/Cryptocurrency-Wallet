from requests import Session
import json
import os

class Price:

    def get_price(symbol):

        key = os.environ['X-CMC_PRO_API_KEY']
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
            'symbol': symbol,
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key,
        }

        session = Session()
        session.headers.update(headers)

        response = session.get(url, params=parameters)
        return float(json.loads(response.text)['data'][symbol]['quote']['USD']['price'])

    def price_list(symbol_list):
        price_list = []
        for n in symbol_list:
            price_list.append(Price.get_price(n))
        return price_list



