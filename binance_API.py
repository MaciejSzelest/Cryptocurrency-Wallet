from binance.client import Client
import pandas as pd
from price_API import Price
import os

# Options
pd.set_option('float_format', '{:f}'.format)

# Parameters
symbol_list = ['ADA', 'BTC', 'ETH', 'SOL']
price_list = ['ADA', 'BTC', 'ETH', 'SOL']
trade_list = ['ADAUSDT', 'BTCUSDT', 'ETHUSDT', 'SOLUSDT']
trading_book = []

class Binance:

    def login():
        api_key = os.environ['api_key']
        api_secret = os.environ['api_secret']
        client = Client(api_key, api_secret)
        return client

    def account():
        client = Binance.login()
        info = client.get_account()
        return info['balances']
        client.close_connection()

    def orders(trade):
        client = Binance.login()
        orders = client.get_all_orders(symbol=trade)
        return orders
        client.close_connection()

    def address(symbol):
        client = Binance.login()
        address = client.get_deposit_address(coin=symbol)
        return address
        client.close_connection()

    def account_snap(account):
        client = Binance.login()
        details = client.get_account_snapshot(type=account)
        return details
        client.close_connection()


class Data:

    def get_account_details():
        # Account details
        account = Binance.account()
        account_balance = pd.DataFrame(account)
        account_balance.drop(columns='locked', inplace=True)
        account_balance = account_balance.rename(columns={'free': 'amount'})
        account_balance['asset'] = account_balance['asset'].astype(str)
        account_balance['amount'] = account_balance['amount'].astype(float)
        account_balance = account_balance[account_balance['asset'].isin(symbol_list)]
        # account_balance.set_index('asset', inplace=True)
        account_balance.sort_values(by='asset', inplace=True)
        return account_balance

    def get_account_value(price_list):
        # Account value as per USDT
        account_value = Data.get_account_details()
        price_tab = Price.price_list(price_list)
        account_value['price'] = price_tab
        account_value['value'] = account_value['amount'] * account_value['price']
        account_value.sort_values(by='asset', inplace=True)
        return account_value

    def get_orders(trade):
        # Trades PNL tab
        trades = Binance.orders(trade)
        price_list = []
        price_amt = []
        for n in trades:
            price_list.append(n['price'])
            price_amt.append(n['executedQty'])

        if trade == 'ADAUSDT':
            trade_price = 'ADA'
        elif trade == 'BTCUSDT':
            trade_price = 'BTC'
        elif trade == 'ETHUSDT':
            trade_price = 'ETH'
        elif trade == 'SOLUSDT':
            trade_price = 'SOL'

        price = float(Price.get_price(trade_price))
        dict_tab = {'amount': price_amt,
                    'price': price_list}
        orders = pd.DataFrame(dict_tab)
        orders[['amount', 'price']] = orders[['amount', 'price']].astype(float)
        orders['PNL'] = (price - orders['price']) * orders['amount']
        orders['asset'] = trade_price
        return orders

    def get_total(ada_tab, btc_tab, eth_tab, sol_tab):
        total_data = {'asset': price_list,
                      'PNL': [ada_tab.PNL.sum(), btc_tab.PNL.sum(), eth_tab.PNL.sum(), sol_tab.PNL.sum()]
                      }
        total_tab = pd.DataFrame(total_data)
        return total_tab