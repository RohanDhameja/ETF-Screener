# Quick Start Guide

## Get Started in 2 Steps!

### Step 1: Start the API Server

**macOS/Linux:**
```bash
./start_server.sh
```

**Windows:**
```bash
start_server.bat
```

Or manually:
```bash
pip install -r requirements.txt
python etf_api.py
```

### Step 2: Open the Web Interface

Simply open `etf-screener.html` in your browser and click **"Load ETF Data"**.

---

## What You'll See

The screener displays the **Top 100 Highest Yielding ETFs** with:

- ✅ Real-time prices from Yahoo Finance
- ✅ 20-day and 50-day moving averages
- ✅ Position analysis (above/below MA)
- ✅ YTD and 1-year returns
- ✅ Trading volume
- ✅ Filterable columns
- ✅ Sortable by any column

---

## Quick Filtering Examples

### Find high-yield ETFs below their 50-day MA (buying opportunities):
1. Set "Position (50MA)" dropdown to "Below MA"
2. Click "YTD Return" column to sort by highest returns

### Find ETFs in a specific price range:
- Enter "100-200" in the Price filter box

### Search for specific ETFs:
- Type "SPY" or "QQQ" in the Symbol filter

### Find strong performers:
- Enter "20" in the YTD Return filter (shows ETFs with ≥20% return)

---

## Data Sources

- **ETFdb.com**: Top ETFs list
- **Yahoo Finance**: Real-time prices, moving averages, returns

---

## Troubleshooting

**"Failed to fetch live data"**: Make sure the Python server is running (`python etf_api.py`)

**Slow loading**: First load takes 30-60 seconds to fetch 100 ETFs. This is normal.

---

For detailed documentation, see `ETF_SCREENER_README.md`

