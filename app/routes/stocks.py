from fastapi import APIRouter, HTTPException
from app.services.stock_services import fetch_stock_data
from app.utils.cleaner import clean_stock_data
from app.services.metrics_service import calculate_metrics

router = APIRouter()

SUPPORTED_COMPANIES = ["AAPL", "MSFT", "GOOGL", "TSLA"]


@router.get("/companies")
def list_companies():
    return {"companies": SUPPORTED_COMPANIES}


@router.get("/stocks/{symbol}")
def get_stock_data(symbol: str):
    symbol = symbol.upper()

    if symbol not in SUPPORTED_COMPANIES:
        raise HTTPException(status_code=404, detail="Stock not supported")

    df = fetch_stock_data(symbol)
    clean_df = clean_stock_data(df)

    return clean_df.tail(30).to_dict(orient="records")


@router.get("/stocks/{symbol}/summary")
def stock_summary(symbol: str):
    symbol = symbol.upper()

    if symbol not in SUPPORTED_COMPANIES:
        raise HTTPException(status_code=404, detail="Stock not supported")

    df = fetch_stock_data(symbol)
    clean_df = clean_stock_data(df)
    metrics = calculate_metrics(clean_df)

    return {
        "symbol": symbol,
        "summary": metrics
    }