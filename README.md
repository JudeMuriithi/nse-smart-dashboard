# NSE Smart Dashboard

A real-time and mock-data **Business Intelligence (BI) dashboard** for monitoring **Nairobi Securities Exchange (NSE)** stock performance — built with **Streamlit** and **Python**.

## Overview

The **NSE Smart Dashboard** provides an interactive way to visualize and analyze stock data from Kenyan companies.  
It supports **mock data** (for offline testing) and can be extended to handle **real-time stock data** via APIs.

You can use this project to:
- Track performance trends of major NSE-listed companies.
- Experiment with Business Intelligence (BI) dashboards.
- Explore the integration of AI-driven analytics (future scope).

---

## Features

Interactive dashboard built with **Streamlit**  
Displays stock performance from mock CSV data  
Simple and extensible structure (easy to adapt for real-time APIs)  
Clean visualization of price changes and company comparisons  
Designed for **AI + BI** integration in the future  

---

## Project Structure

nse-smart-dashboard/
│
├── dashboard.py # Main Streamlit dashboard app
├── fetch_mock_data.py # Generates mock stock data
├── mock_stock_data.csv # Sample dataset for offline use
├── fetch_realtime.py # Script for live data fetching
├── requirements.txt # Dependencies list
└── README.md # Project documentation


---

## Installation & Setup

### 1. Clone this repository
git clone https://github.com/JudeMuriithi/nse-smart-dashboard.git

### 2. Create a virtual environment
pip install -r requirements.txt

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the dashboard
streamlit run dashboard.py


## Future Enhancements

Integrate AI predictions (e.g., future price trends)

Add real-time NSE API data

Include data export and alerts

Host the app online (e.g., Streamlit Cloud)