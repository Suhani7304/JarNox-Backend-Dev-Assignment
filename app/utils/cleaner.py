import pandas as pd


def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw stock data:
    - Converts Date index to column
    - Formats Date
    - Handles missing values
    - Drops unnecessary columns
    """

    # Convert Date index to column
    df = df.reset_index()

    # Rename Date column (sometimes it's 'Date' or 'Datetime')
    df.rename(columns={"Datetime": "Date"}, inplace=True)

    # Format Date
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

    # Keep only useful columns
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]

    # Handle missing values (forward fill)
    df.fillna(method="ffill", inplace=True)

    return df