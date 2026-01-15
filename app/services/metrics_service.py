import pandas as pd


def calculate_metrics(df: pd.DataFrame) -> dict:
    """
    Calculates stock market metrics from cleaned data
    """

    # Daily Return
    df["Daily_Return"] = df["Close"].pct_change()

    # 7-Day Moving Average
    df["7_Day_MA"] = df["Close"].rolling(window=7).mean()

    # 52-week high & low
    high_52 = df["High"].max()
    low_52 = df["Low"].min()

    # Volatility (standard deviation of daily returns)
    volatility = df["Daily_Return"].std()

    return {
        "52_week_high": round(high_52, 2),
        "52_week_low": round(low_52, 2),
        "volatility": round(volatility, 4),
        "latest_7_day_moving_avg": round(df["7_Day_MA"].iloc[-1], 2)
    }