import mplfinance as mpf
import yfinance as yf
import pandas as pd

# Step 1: Data Extraction
def extract_stock_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        return data
    except Exception as e:
        print("Error occurred during data extraction:", e)
        return None

# Step 2: Data Processing
def calculate_average_volume(data):
    if data is None:
        return None
    try:
        average_volume = data['Volume'].mean()
        return average_volume
    except Exception as e:
        print("Error occurred during data processing:", e)
        return None

# Step 3: Data Visualization
def visualize_stock_data(data):
    if data is None:
        return
    mpf.plot(data, type='candle', volume=True, style='yahoo')

# Example usage
if __name__ == '__main__':
    # Specify the stock symbol, start date, and end date
    si=input("please type stock symbol")
    symbol = si.upper()  # Replace with your desired stock symbol
    start_date = '2022-07-01'
    end_date = '2023-06-30'

    # Extract stock data
    stock_data = extract_stock_data(symbol, start_date, end_date)

    # Calculate average daily trading volume
    average_volume = calculate_average_volume(stock_data)
    if average_volume is not None:
        print("Average Daily Trading Volume:", average_volume)

    # Visualize stock data
    visualize_stock_data(stock_data)
