import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
from sklearn.linear_model import LinearRegression

# --- Page Setup ---
st.set_page_config(page_title="NSE Smart Dashboard (AI + BI)", layout="wide")

# --- Load mock data ---
@st.cache_data
def load_data():
    return pd.read_csv("mock_stock_data.csv")

data = load_data()
data["Date"] = pd.to_datetime(data["Date"])

# --- Title ---
st.title("🤖 NSE Smart Dashboard — AI + BI Edition")
st.caption("Real-time simulation with AI-driven trend prediction using mock NSE data")

# --- Sidebar ---
companies = data["Company"].unique()
selected_company = st.sidebar.selectbox("Select Company", companies)
refresh_rate = st.sidebar.slider("Auto-refresh every (seconds)", 5, 60, 10)

# --- Placeholder for live updates ---
placeholder = st.empty()

# --- Live Simulation Loop ---
for _ in range(1000):
    temp_data = data.copy()

    # Random price variations for realism
    temp_data["Price"] = temp_data["Price"] * np.random.uniform(0.99, 1.01, len(temp_data))

    # Filter for chosen company
    filtered = temp_data[temp_data["Company"] == selected_company].reset_index(drop=True)

    # --- AI Trend Prediction ---
    X = np.arange(len(filtered)).reshape(-1, 1)
    y = filtered["Price"].values

    model = LinearRegression()
    model.fit(X, y)
    next_index = np.array([[len(filtered) + 1]])
    predicted_price = model.predict(next_index)[0]

    latest_price = filtered["Price"].iloc[-1]
    trend = "📈 Upward" if predicted_price > latest_price else "📉 Downward"
    confidence = abs((predicted_price - latest_price) / latest_price) * 100

    # --- Display section ---
    with placeholder.container():
        st.subheader(f"📊 {selected_company} Stock Overview")
        st.line_chart(filtered.set_index("Date")["Price"], height=300)

        col1, col2, col3 = st.columns(3)
        col1.metric("Current Price", f"Ksh {latest_price:.2f}")
        col2.metric("Predicted Next Price", f"Ksh {predicted_price:.2f}")
        col3.metric("AI Trend Prediction", f"{trend} ({confidence:.2f}% confidence)")

        st.caption(f"Last updated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    time.sleep(refresh_rate)
