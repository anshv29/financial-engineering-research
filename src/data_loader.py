import yfinance as yf
import pandas as pd
from sqlalchemy import text
from database import get_engine

TICKERS = [
    'SPY', 'AAPL', 'MSFT', 'GOOGL', 'AMZN',
    'META', 'NVDA', 'JPM', 'GS', 'BAC',
    'XOM', 'JNJ', 'UNH', 'V', 'MA'
]

START_DATE = "2014-01-01"
END_DATE = "2024-12-31"

def create_price_table():
    engine = get_engine()
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS stock_prices (
        date DATE NOT NULL,
        ticker VARCHAR(10) NOT NULL,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume BIGINT,
        PRIMARY KEY (date, ticker)
    );
    """
    with engine.connect() as conn:
        conn.execute(text(create_table_sql))
        conn.commit()
    print("Table created successfully!")

def pull_and_store_data():
    engine = get_engine()
    
    for ticker in TICKERS:
        print(f"Pulling data for {ticker}...")
        
        df = yf.download(ticker, start=START_DATE, end=END_DATE, auto_adjust=True)
        
        df = df.reset_index()
        df.columns = df.columns.get_level_values(0)
        df.columns = [c.lower() for c in df.columns]
        df['ticker'] = ticker
        df = df[['date', 'ticker', 'open', 'high', 'low', 'close', 'volume']]
        df['date'] = pd.to_datetime(df['date']).dt.date
        
        df.to_sql(
            'stock_prices',
            engine,
            if_exists='append',
            index=False,
            method='multi'
        )
        print(f"{ticker} stored! {len(df)} rows saved.")
    
    print("\nAll data loaded successfully!")

if __name__ == "__main__":
    create_price_table()
    pull_and_store_data()