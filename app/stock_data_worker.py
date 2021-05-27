from datetime import date, datetime

import yfinance as yf
from pymongo import DESCENDING

from app.common import mongo


def initialize_stock_data(ticker: str):
    today = date.today().isoformat()
    data = yf.download(ticker.upper(), start='2019-01-02', end=today)
    for key, value in data.T.to_dict().items():
        value['Date'] = key
        mongo.client[f'{ticker}_stocks'].insert(value)


def upsert_stock_data(ticker: str, last_date: datetime):
    today = date.today().isoformat()
    data = yf.download(ticker.upper(), start=last_date.strftime("%Y-%m-%d"), end=today)
    for key, value in data.T.to_dict().items():
        value['Date'] = key
        mongo.client[f'{ticker}_stocks'].update({"Date": key}, value, upsert=True)


def run():
    tickers = mongo.client['tickers'].find()
    for item in list(tickers):
        ticker = item.get("ticker")
        data = mongo.client[f'{ticker}_stocks'].find()

        if len(list(data)) == 0:
            initialize_stock_data(ticker)
        else:
            data = mongo.client[f'{ticker}_stocks'].find().sort("Date", DESCENDING).limit(1)
            upsert_stock_data(ticker, list(data)[0].get('Date'))
