from fastapi import FastAPI
from app.routes.stocks import router as stock_router

app = FastAPI(
    title="Stock Market Data Platform",
    description="Backend API for stock market data analysis",
    version="1.0.0"
)

app.include_router(stock_router)