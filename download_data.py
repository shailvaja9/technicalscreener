import configparser
import yfinance as yf
import pandas as pd

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Access configuration options
start_date = config['DEFAULT']['start_date']
end_date = config['DEFAULT']['end_date']
tickers = config['STOCKS']['tickers'].split(', ')  # Assuming tickers are separated by ", "

def download_stock_data(tickers):
    for ticker in tickers:
        print(f"Downloading data for {ticker}")
        data = yf.download(ticker, start=start_date, end=end_date)
        if not data.empty:
            data.to_parquet(f"{ticker}_data.parquet")
            print(f"Data for {ticker} saved to Parquet.")
        else:
            print(f"No data found for {ticker}")

if __name__ == "__main__":
    download_stock_data(tickers)
