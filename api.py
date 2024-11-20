from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time
import random
from typing import Generator
from datetime import datetime

app = FastAPI()

stock_prices = {
    "USD": 100.0,
    "AAPL": 150.0,
    "GOOGL": 2800.0
}


def simulate_price_change(current_price: float) -> float:
    """Simulates a small price change to mimic real-time market fluctuations."""
    return round(current_price + random.uniform(-1.0, 1.0), 2)


def stock_price_stream(symbol: str) -> Generator[str, None, None]:
    """Generator function to stream stock data."""
    if symbol not in stock_prices:
        yield f"{{\"error\": \"Share {symbol} not found.\"}}\n"
        return

    price = stock_prices[symbol]
    while True:
        price = simulate_price_change(price)
        timestamp = datetime.utcnow().isoformat()
        stock_prices[symbol] = price
        yield f"{{\"symbol\": \"{symbol}\", \"price\": {price}, \"timestamp\": \"{timestamp}\"}}\n"
        time.sleep(1)


@app.get("/stocks/{symbol}")
def get_stock_price(symbol: str):
    """API endpoint to stream stock price data."""
    return StreamingResponse(stock_price_stream(symbol), media_type="text/event-stream")
