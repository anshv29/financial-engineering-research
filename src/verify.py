from database import get_engine
import pandas as pd

engine = get_engine()

df = pd.read_sql("SELECT ticker, COUNT(*) as rows, MIN(date) as start, MAX(date) as end FROM stock_prices GROUP BY ticker ORDER BY ticker", engine)

print(df.to_string())