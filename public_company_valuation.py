import yfinance as yf

# Define public competitors' tickers
tickers = ["NVDA", "AMD", "INTC", "QCOM"]
data = {}

# Fetch 6-month historical stock prices
for ticker in tickers:
    stock_data = yf.download(ticker, start="2024-08-02", end="2025-02-02")
    data[ticker] = stock_data

# Save to CSV
for ticker, df in data.items():
    df.to_csv(f"{ticker}_6_month_stock_prices.csv")
