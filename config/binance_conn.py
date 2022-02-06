import pandas as pd
import requests


def get_ticker_price(ticker):
    """
    Gets current price from Binance API
    :param ticker: symbol to check
    :return: prince (float)
    """
    url = 'https://api.binance.com/api/v3/ticker/price'

    params = {'symbol': ticker}

    r = requests.get(url, params=params)
    js = r.json()

    price = js.get('price')
    price = float(price)

    return price

# print((get_ticker_price('ADAUSDT')))


def get_historic_data(symbol, interval='1d', startTime=None, endTime=None, limit=1000):
    """
        Getting historic Data from Binance API
    :param symbol: ticker (BTCUSDT, ETHUSDT, etc..)
    :param interval:
        Minutes: 1m, 2m, 3m, 15m, 30m
        Hours: 1h, 2h, 4h
        Days: 1d, 3d
        Month: 1M
    :param startTime: time in ms
    :param endTime: time in ms
    :param limit: row limits (1000 default)
    :return: DataFrame with OHLC price history
    """

    url = 'https://api.binance.com/api/v3/klines'

    params = {'symbol': symbol, 'interval': interval,
              'startTime': startTime, 'endTime': endTime, 'limit': limit}

    r = requests.get(url, params=params)
    js = r.json()

    # Creating Dataframe
    cols = ['openTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'cTime',
            'qVolume', 'trades', 'takerBase', 'takerQuote', 'Ignore']

    df = pd.DataFrame(js, columns=cols)

    # Converting strings to numeric
    df = df.apply(pd.to_numeric)

    # Timestamp Index handling
    df.index = pd.to_datetime(df.openTime, unit='ms')

    # Dropping unused columns
    df = df.drop(['openTime', 'cTime', 'takerBase', 'takerQuote', 'Ignore'], axis=1)
    df = df.drop(['trades', 'qVolume'], axis=1)

    return df




