# fetch_data.py — verbose debug version
import yfinance as yf
import pandas as pd
from datetime import datetime
import sys
import traceback

# --- List of Kenyan stocks (Yahoo Finance tickers) ---
stocks = {
    "Safaricom": "SCOM.NR",
    "KCB Group": "KCB.NR",
    "Equity Group": "EQTY.NR",
    "Cooperative Bank": "COOP.NR",
    "NCBA Group": "NCBA.NR"
}

def try_download_with_history(symbol):
    """Try Ticker.history first (preferred). Return DataFrame or None."""
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1d", interval="1m")  # try intraday first
        if hist is None or hist.empty:
            # try daily history
            hist = ticker.history(period="1d")
        return hist
    except Exception:
        return None

def try_download_with_download(symbol):
    """Fallback to yf.download"""
    try:
        df = yf.download(symbol, period="1d", interval="1m", progress=False)
        if df is None or df.empty:
            df = yf.download(symbol, period="1d", progress=False)
        return df
    except Exception:
        return None

def get_nse_data(verbose=True):
    """Fetch real-time stock data for selected Kenyan companies."""
    data = []
    if verbose:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting fetch for {len(stocks)} stocks...")

    for name, symbol in stocks.items():
        if verbose:
            print(f"\n-- Fetching {name} ({symbol}) --")
        try:
            hist = try_download_with_history(symbol)
            if (hist is None) or hist.empty:
                if verbose:
                    print(f"  history() returned empty — trying download() fallback for {symbol}")
                hist = try_download_with_download(symbol)

            if (hist is None) or hist.empty:
                print(f"  !! No data returned for {symbol}. Skipping.")
                continue

            # Ensure DataFrame has at least one row
            latest = hist.iloc[-1]
            row = {
                "Company": name,
                "Symbol": symbol,
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Open": round(float(latest.get("Open", 0)), 2),
                "Close": round(float(latest.get("Close", 0)), 2),
                "High": round(float(latest.get("High", 0)), 2),
                "Low": round(float(latest.get("Low", 0)), 2),
                "Volume": int(latest.get("Volume", 0) or 0)
            }
            data.append(row)
            if verbose:
                print("  Success:", row)
        except Exception as e:
            print(f"  Error fetching {symbol}: {e}")
            traceback.print_exc()

    df = pd.DataFrame(data)
    if verbose:
        print("\nFetch complete.")
        if df.empty:
            print("WARNING: no rows collected (df is empty). Possible reasons: no internet, yfinance rate-limit, or tickers unavailable on Yahoo.")
        else:
            print(df.to_string(index=False))
    return df

if __name__ == "__main__":
    try:
        df = get_nse_data(verbose=True)
        # Save to CSV for quick inspection
        if not df.empty:
            csv_name = "nse_sample_latest.csv"
            df.to_csv(csv_name, index=False)
            print(f"\nSaved latest sample to {csv_name}")
        else:
            print("\nNo data saved because dataframe is empty.")
    except Exception as e:
        print("Fatal error while fetching data:", e)
        traceback.print_exc()
        sys.exit(1)
