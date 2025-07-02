import yfinance as yf
import pandas as pd

def download_stock_data(ticker="AAPL", start="2015-01-01", end="2024-01-01"):
    df = yf.download(ticker, start=start, end=end)
    return df[['Close']]

def save_to_csv(df, path):
    df.to_csv(path)

def load_from_csv(path):
    return pd.read_csv(path, index_col='Date', parse_dates=True)
