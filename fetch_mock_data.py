import random
import time
from datetime import datetime
import pandas as pd

def generate_mock_data():
    stocks = {
        "Safaricom": round(random.uniform(15, 25), 2),
        "KCB Group": round(random.uniform(30, 45), 2),
        "Equity Group": round(random.uniform(35, 50), 2),
        "Cooperative Bank": round(random.uniform(12, 18), 2),
        "NCBA Group": round(random.uniform(32, 40), 2)
    }

    data = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for name, price in stocks.items():
        data.append({"Company": name, "Price": price, "Timestamp": timestamp})
    
    df = pd.DataFrame(data)
    df.to_csv("mock_stock_data.csv", index=False)
    print(f"[{timestamp}] ✅ Mock NSE data generated successfully.")
    print(df)

if __name__ == "__main__":
    print("Generating mock NSE stock data every 10 seconds...")
    while True:
        generate_mock_data()
        time.sleep(10)
