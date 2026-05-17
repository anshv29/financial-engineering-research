# Quantitative Factor Research Platform

A full-stack quantitative research system built in Python, designed to evaluate whether factor-based 
investing strategies can outperform passive index investing. Built with a real PostgreSQL database, 
a backtesting engine, and machine learning models (XGBoost + LSTM).

---

## Results

| Strategy | Total Return | Sharpe Ratio | Max Drawdown |
|---|---|---|---|
| Long Factor Portfolio | 1,398.7% | 1.598 | -21.1% |
| SPY Benchmark | 251.0% | 0.873 | -23.9% |
| Short Factor Portfolio | 442.2% | 0.825 | -36.4% |

---

## Project Structure

## Tech Stack

- **Python 3.14**
- **PostgreSQL 18** — persistent market data storage
- **SQLAlchemy + psycopg2** — database ORM and connection
- **pandas, numpy, scipy** — data engineering and statistics
- **yfinance** — market data sourcing
- **scikit-learn, XGBoost** — machine learning
- **PyTorch** — LSTM neural network
- **matplotlib** — visualization and tearsheet generation

---

## Methodology

### Phase 1 — Data Infrastructure
Built a PostgreSQL database storing 10 years of daily OHLCV data for 15 stocks (2014–2024), totalling
41,505 rows.

### Phase 2 — Factor Engineering
Engineered 12 alpha factors across four categories:
- **Momentum** — 12m, 6m, 1m returns and short term reversal
- **Volatility** — realized vol (21d, 63d) and volatility ratio
- **Volume** — volume ratio and price volume trend
- **Mean Reversion** — distance from 52 week high and RSI (Relative Strength Index)

### Phase 3 — Backtesting Engine
Monthly rebalancing across 119 periods (2015–2024). Stocks ranked by combined factor score, long 
portfolio holds top 5, short portfolio tracks bottom 5. Metrics include total return, 
annualized return, Sharpe ratio, max drawdown, and win rate.

### Phase 4 — Machine Learning
- **XGBoost** with walk forward validation
- **LSTM Neural Network** using 6 month sequences of factor data
- Both models achieved ~50% accuracy, consistent with semi-efficient markets on a small sample size.

### Phase 5 — Tearsheet
Institutional grade research tearsheet including cumulative performance, metrics table, 
monthly returns heatmap, drawdown analysis, and ML results.

---

## Key Findings

1. Long portfolio returned **1,398.7%** vs SPY's **251.0%** over 10 years
2. Sharpe ratio of **1.598** vs SPY's **0.873** — better risk-adjusted returns
3. Max drawdown of **-21.1%** vs SPY's **-23.9%** — less severe crashes despite higher returns
4. XGBoost and LSTM both achieved ~50% accuracy on a 15 stock sample  — ML adds marginal 
predictive value over the factor model alone on small universes
5. The edge comes from **systematic rebalancing**, not individual stock picking
6. A universe of **500+ stocks** would be needed for production-grade statistical robustness

---

## Disclaimer
This project is for educational and research purposes only. Nothing here constitutes financial advice.
