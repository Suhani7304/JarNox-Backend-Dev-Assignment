from app.utils.cleaner import clean_stock_data
from app.services.stock_services import fetch_stock_data
from app.utils.cleaner import clean_stock_data
from app.services.metrics_service import calculate_metrics

df = fetch_stock_data("AAPL")
clean_df = clean_stock_data(df)
metrics = calculate_metrics(clean_df)

print(metrics)


# df = fetch_stock_data("AAPL")
# clean_df = clean_stock_data(df)

# print(clean_df.head())
# print(clean_df.columns)


# df = fetch_stock_data("AAPL")
# print(df.head())
# print(df.columns)