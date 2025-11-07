# 📊 ETF Screener Dashboard

A powerful web-based ETF screening tool that fetches **live data** from Yahoo Finance, displaying the top 100 highest-yielding ETFs with advanced filtering, sorting, and moving average analysis.

![ETF Screener](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- ✅ **Live Data**: Real-time ETF data from Yahoo Finance
- 📈 **Moving Averages**: 20-day and 50-day moving averages
- 🎯 **Smart Filtering**: Filter by symbol, price range, position relative to MA, returns
- 🔄 **Sortable Columns**: Click any column header to sort
- 💹 **Return Analysis**: YTD and 1-year return rates
- 📊 **Position Analysis**: Identify ETFs above/below their moving averages
- 🎨 **Modern UI**: Beautiful, responsive design

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/etf-screener.git
cd etf-screener
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Start the API server**
```bash
python etf_api.py
```

4. **Open the web interface**
- Open `etf-screener.html` in your web browser
- Click "Load ETF Data"
- Wait 30-60 seconds for data to load

### Alternative: Use startup scripts

**macOS/Linux:**
```bash
./start_server.sh
```

**Windows:**
```bash
start_server.bat
```

## 📖 Usage

### Finding Investment Opportunities

**High-yield ETFs below 50-day MA (potential buying opportunities):**
1. Set "Position (50MA)" dropdown to "Below MA"
2. Click "YTD Return" column header to sort by highest returns

**Strong momentum ETFs:**
1. Enter "20" in the YTD Return filter
2. Sort by "1Y Return"

**Specific price range:**
- Enter "100-200" in the Price filter box

**Search for specific ETFs:**
- Type "SPY" or "QQQ" in the Symbol filter

### Filter Examples

- **Symbol**: `SPY` - Find specific ETF
- **Price**: `50-150` - ETFs between $50-$150
- **Position (50MA)**: Select "Below MA" - ETFs below their 50-day moving average
- **Position (20MA)**: Select "Above MA" - ETFs above their 20-day moving average
- **YTD Return**: `20` - ETFs with at least 20% year-to-date return
- **1Y Return**: `15` - ETFs with at least 15% one-year return

## 📊 Data Sources

- **Yahoo Finance**: Real-time prices, historical data, moving averages
- **Curated List**: Top 100 most popular ETFs including:
  - Major indices (SPY, QQQ, IWM, VTI, VOO, IVV)
  - International (VEA, IEMG, VWO, EEM)
  - Sector ETFs (XLF, XLE, XLK, XLV, XLI, XLP, XLU, XLY, XLB, XLC)
  - Commodities (GLD, SLV, GDX)
  - Bonds (AGG, BND, TLT, LQD, HYG)

## 🏗️ Architecture

### Backend (Python)
- **Flask**: Web server framework
- **yfinance**: Yahoo Finance API wrapper
- **pandas**: Data analysis and manipulation
- **BeautifulSoup4**: Web scraping capabilities
- **ThreadPoolExecutor**: Parallel data fetching for performance

### Frontend (JavaScript)
- Vanilla JavaScript (no frameworks)
- Live API integration
- Client-side filtering and sorting
- Responsive CSS design

## 📡 API Endpoints

The Flask backend provides these REST API endpoints:

- `GET /api/etfs` - Fetch all ETF data (top 100)
- `GET /api/etf/<symbol>` - Fetch data for a specific ETF
- `GET /api/health` - Health check

### Example API Response

```json
{
  "success": true,
  "count": 100,
  "data": [
    {
      "symbol": "SPY",
      "name": "SPDR S&P 500 ETF Trust",
      "price": 450.32,
      "ma20": 448.50,
      "ma50": 445.20,
      "returnRate": 18.5,
      "yearReturn": 22.3,
      "volume": 75000000,
      "belowMA50": false,
      "belowMA20": false
    }
  ],
  "timestamp": "2025-11-06T20:22:47.123456",
  "source": "ETFdb.com + Yahoo Finance"
}
```

## 🔧 Configuration

### Change API Port

If port 8000 is in use, modify `etf_api.py`:

```python
app.run(debug=True, host='0.0.0.0', port=8001)  # Change to desired port
```

And update `etf-screener.html`:

```javascript
const response = await fetch('http://localhost:8001/api/etfs');
```

### Customize ETF List

Edit the `get_fallback_etfs()` function in `etf_api.py` to add/remove ETFs.

## 🐛 Troubleshooting

### "Failed to fetch live data from API"
**Solution**: Make sure the Python API server is running:
```bash
python etf_api.py
```

### Port 8000 already in use
**Solution**: Change the port in `etf_api.py` (see Configuration section)

### Slow data loading
**Normal behavior**: First load takes 30-60 seconds to fetch data for 100 ETFs from Yahoo Finance.

### Missing data for some ETFs
Some ETFs may not have sufficient historical data (50+ days) for moving average calculations and will be excluded.

## 📋 Requirements

See `requirements.txt`:
- flask>=3.0.0
- flask-cors>=4.0.0
- yfinance>=0.2.32
- pandas>=2.2.0
- beautifulsoup4>=4.12.0
- requests>=2.31.0

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for informational and educational purposes only. It is not financial advice. Always do your own research and consult with a qualified financial advisor before making investment decisions.

## 🙏 Acknowledgments

- [Yahoo Finance](https://finance.yahoo.com/) for providing financial data
- [yfinance](https://github.com/ranaroussi/yfinance) Python library
- [Flask](https://flask.palletsprojects.com/) web framework

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

**Made with ❤️ for ETF investors**

