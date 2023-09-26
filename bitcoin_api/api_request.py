# api_request.py

import requests
from config import COINMARKETCAP_API_KEY

BASE_URL = 'https://pro-api.coinmarketcap.com/v1/'

def get_latest_crypto_price():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }
    
    params = {
        'start': '1',
        'limit': '5',
        'convert': 'USD'
    }
    
    response = requests.get(BASE_URL + 'cryptocurrency/listings/latest', headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_top_5(data):
    # Extracting relevant data for display
    for coin in data['data']:
        name = coin['name']
        symbol = coin['symbol']
        price = coin['quote']['USD']['price']
        percent_change_24h = coin['quote']['USD']['percent_change_24h']

        print(f"Name: {name}")
        print(f"Symbol: {symbol}")
        print(f"Price: ${price:,.2f}")
        print(f"24h Change: {percent_change_24h:.2f}%")
        print("-" * 30)

if __name__ == '__main__':
    result = get_latest_crypto_price()

    if result:
        display_top_5(result)
    else:
        print("Failed to retrieve data from CoinMarketCap.")
