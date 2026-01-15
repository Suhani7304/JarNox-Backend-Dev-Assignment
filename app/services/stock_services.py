import yfinance as yf
import pandas as pd


def fetch_stock_data(symbol: str, period: str = "1y") -> pd.DataFrame:
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df