import requests
import pandas as pd

def fetch_data_from_binance(symbol, interval, limit):
    """
    Fetch historical price data from Binance and create a DataFrame.

    Parameters:
    - symbol: String. Symbol for the cryptocurrency (e.g., 'BTCUSDT').
    - interval: String. Time interval for the data (e.g., '1d' for daily).
    - limit: Integer. Number of data points to fetch.

    Returns:
    - df: pandas DataFrame containing the fetched data.
    """
    # Construct the URL for the API request
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    
    # Fetch the data
    data = requests.get(url).json()
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
    
    return df

# Example usage
symbol = "PEPEUSDT"  # Just an example, ensure the symbol is valid on Binance
interval = "1d"  # For example, '1d' for daily intervals
limit = 500  # Number of data points

# Fetch the data
df = fetch_data_from_binance(symbol, interval, limit)

# Further processing can be done on df, such as renaming columns, converting datatypes, etc.
print(df.head())


def rename_columns(df):
    """
    Rename DataFrame columns: convert to lowercase and replace spaces with underscores.

    Parameters:
    - df: pandas DataFrame.

    Returns:
    - df: DataFrame with updated column names.
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_', regex=False)
    return df


def convert_to_datetime(df, datetime_cols):
    """
    Convert specified columns of a DataFrame to datetime.

    Parameters:
    - df: pandas DataFrame.
    - datetime_cols: List of column names to convert to datetime.

    Returns:
    - df: DataFrame with datetime converted columns.
    """
    for col in datetime_cols:
        df[col] = pd.to_datetime(df[col], unit='ms')
    return df


def convert_to_numeric(df, numeric_cols):
    """
    Convert specified columns of a DataFrame to numeric types.

    Parameters:
    - df: pandas DataFrame.
    - numeric_cols: List of column names to convert to numeric.

    Returns:
    - df: DataFrame with numeric converted columns.
    """
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
    return df
