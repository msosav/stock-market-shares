# Stock Market Shares Streaming API

This is a **fake stock market streaming API** built using FastAPI. It simulates real-time stock data for various shares, providing updates on their prices with gradual changes to mimic realistic market behavior.

## Features

- Simulates real-time data for stock market shares.
- Provides stock name, current price, and a timestamp in JSON format.
- Ensures price changes are gradual to reflect real market trends.
- Implements a streaming response for continuous updates.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/msosav/stock-market-shares.git
   cd stock-market-shares
   ```

2. Install dependencies:
   ```bash
   pip install fastapi[standard]
   ```

## Usage

1. Run the application:

   ```bash
   fastapi run apy.py
   ```

2. Access the API:
   - For stock `USD`: `http://127.0.0.1:8000/stocks/USD`
   - Replace `USD` with any stock symbol (e.g., `AAPL`, `GOOGL`) to fetch data for that stock.

## API Endpoints

### Stream Stock Data

- **GET** `/stocks/{symbol}`
  - **Path Parameter**:
    - `symbol` (string): The stock symbol you want to track (e.g., `USD`, `AAPL`).
  - **Response**:
    - A continuous stream of JSON objects containing:
      - `symbol`: The stock symbol.
      - `price`: The current stock price.
      - `timestamp`: ISO-formatted UTC timestamp.

Example response (streaming):

```json
{"symbol": "USD", "price": 100.45, "timestamp": "2024-11-20T12:34:56.789Z"}
{"symbol": "USD", "price": 99.87, "timestamp": "2024-11-20T12:34:57.789Z"}
...
```

## Customization

- To add more stocks, modify the `stock_prices` dictionary in `api.py`:

  ```python
  stock_prices = {
      "USD": 100.0,
      "AAPL": 150.0,
      "GOOGL": 2800.0,
      "NEWSTOCK": 500.0  # Add new stocks here
  }
  ```

- To change the speed or range of price changes, adjust the `simulate_price_change` function.
