import pandas as pd

import config.google_sheets_conn as db
import config.binance_conn as binance


def main():
    # Getting list of tickers
    tickers_db = get_tickers()
    tickers_list = list()

    # Format cryptos
    for ticker in tickers_db:
        tickers_list.append(ticker[0] + 'USDT')

    tickers = ('BTCUSDT', 'ADAUSDT')

    # Get prices
    for ticker in tickers_list:
        price = binance.get_ticker_price(ticker)
        print(ticker, price)


def get_tickers():
    """
    Get list of ticker from google sheets
    :return:
    """

    sheet_id = '1Ai209GagEF30giH0xbSQhaXHFSqpJvcvliv-MCKA6kI'
    sheet_range = "crypto_list!B3:Z"

    data = db.checkSheet(sheet_id, sheet_range)

    return data


if __name__ == main():
    main()
