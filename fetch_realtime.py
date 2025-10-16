import yfinance as yf
import pandas as pd
from datetime import datetime

symbols = {
    "Safaricom": "SCOM.NSE",
    "KCB Group": "KCB.NSE",
    "Equity Group": "EQTY.NSE",
    "Cooperative Bank": "COOP.NSE",
    "NCBA Group": "NCBA.NSE"
}

def fetch_data():
    print(f"[{datetime.now()}] Fetching NSE stock data via Yahoo Finance...\n")
    all_data = []

    for name, symbol in symbols.items():
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(period="1d", interval="1h")

            if df.empty:
                print(f"⚠️ No data found for {name} ({symbol})\n")
                continue

            latest = df.tail(1).iloc[0]
            price = round(latest['Close'], 2)
            change = round(latest['Close'] - latest['Open'], 2)
            pct_change = round((change / latest['Open']) * 100, 2)

            all_data.append({
                "Company": name,
                "Symbol": symbol,
                "Price": price,
                "Change": change,
                "% Change": pct_change
            })
            print(f"✅ {name}: {price} KES ({pct_change}%)")

        except Exception as e:
            print(f"❌ Error fetching {name} ({symbol}): {e}\n")

    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv("nse_live_data.csv", index=False)
        print("\n💾 Saved latest NSE data to nse_live_data.csv")
        print(df)
    else:
        print("\n⚠️ No data fetched.")

if __name__ == "__main__":
    fetch_data()
