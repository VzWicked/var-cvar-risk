"""Download price data and compute returns."""

from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

RAW_DIR = Path("data/raw")


def download_prices(tickers, start, end):
    """Download adjusted prices and save them to the data/raw/prices.csv"""
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)
    prices = data["Close"]
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    prices.to_csv(RAW_DIR / "prices.csv")
    return prices


def compute_returns(prices, kind="log"):
    """Return daily log or simple returns, dropping the first (empty) row"""
    if kind =="simple":
        returns = (prices - prices.shift(1)) / prices.shift(1)

    elif kind == "log":
        returns = np.log(prices / prices.shift(1))

    else:
        raise ValueError(f"kind must be 'log' or 'simple', got {kind!r}")

    return returns.dropna()


if __name__ == "__main__":
    prices = download_prices(["SPY", "QQQ", "TLT", "GLD"], "2005-01-01", "2025-01-01")
    log_r = compute_returns(prices, "log")
    print(prices.tail())
    print(log_r.describe())