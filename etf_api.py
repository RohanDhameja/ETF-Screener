"""
ETF Data API Server
Fetches live ETF data from ETFdb.com and Yahoo Finance
"""

from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import time
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for browser access

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_top_etfs_from_etfdb():
    """Fetch top ETFs list from ETFdb.com"""
    try:
        logger.info("Fetching top ETFs from ETFdb.com...")
        
        # ETFdb screener URL - fetching top ETFs by AUM
        url = "https://etfdb.com/screener/"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try to extract ETF symbols from the page
            symbols = []
            
            # Look for ticker symbols in the page
            links = soup.find_all('a', href=re.compile(r'/etf/[A-Z]+/'))
            for link in links:
                match = re.search(r'/etf/([A-Z]+)/', link['href'])
                if match:
                    symbol = match.group(1)
                    if symbol not in symbols and len(symbol) <= 5:
                        symbols.append(symbol)
            
            if symbols:
                logger.info(f"Found {len(symbols)} ETFs from ETFdb.com")
                return symbols[:100]  # Return top 100
        
        # Fallback to popular ETFs if scraping fails
        logger.warning("Could not scrape ETFdb.com, using fallback list")
        return get_fallback_etfs()
        
    except Exception as e:
        logger.error(f"Error fetching from ETFdb.com: {str(e)}")
        return get_fallback_etfs()


def get_fallback_etfs():
    """Return a curated list of top 100 ETFs"""
    return [
        'SPY', 'QQQ', 'IWM', 'EEM', 'VTI', 'EFA', 'GLD', 'HYG', 'LQD', 'AGG',
        'VOO', 'VEA', 'IEMG', 'IJH', 'VWO', 'SLV', 'TLT', 'IVV', 'BND', 'VTV',
        'IJR', 'XLF', 'VUG', 'IEFA', 'VIG', 'VB', 'XLE', 'VNQ', 'GDX', 'TIP',
        'VGT', 'VO', 'BNDX', 'VCIT', 'VYM', 'XLK', 'VCSH', 'XLV', 'XLI', 'XLP',
        'DIA', 'IWF', 'VT', 'EMB', 'IWD', 'SCHF', 'XLU', 'XLY', 'USMV', 'QUAL',
        'RSP', 'VBR', 'VXF', 'SCHX', 'IWB', 'MDY', 'VBK', 'ITOT', 'VXUS', 'SCHA',
        'XLB', 'SCHD', 'VGK', 'IWP', 'SCHE', 'VEU', 'SPDW', 'SPEM', 'DGRO', 'IYR',
        'IWN', 'IUSB', 'XLC', 'MBB', 'GOVT', 'PFF', 'SHY', 'IWV', 'DVY', 'SDY',
        'IWS', 'MGC', 'VV', 'IVW', 'MGK', 'SCHG', 'IWR', 'SCHB', 'VTEB', 'SLYV',
        'SPYG', 'IWO', 'VCR', 'VDC', 'SPSM', 'VTIP', 'IEF', 'VHT', 'SPYV', 'SPTM'
    ]


def fetch_etf_data_from_yfinance(symbol, retries=3):
    """Fetch detailed ETF data from Yahoo Finance with retry logic"""
    for attempt in range(retries):
        try:
            # Add small delay to avoid rate limiting
            if attempt > 0:
                wait_time = (2 ** attempt) * 0.5  # Exponential backoff: 0.5s, 1s, 2s
                time.sleep(wait_time)
                logger.info(f"Retry {attempt + 1}/{retries} for {symbol} after {wait_time}s delay")
            
            ticker = yf.Ticker(symbol)
            
            # Get historical data for moving averages
            hist = ticker.history(period='3mo')
            
            if hist.empty or len(hist) < 50:
                logger.warning(f"Insufficient data for {symbol}")
                return None
            
            # Get current price
            current_price = hist['Close'].iloc[-1]
            
            # Calculate moving averages
            ma20 = hist['Close'].rolling(window=20).mean().iloc[-1]
            ma50 = hist['Close'].rolling(window=50).mean().iloc[-1]
            
            # Calculate returns
            try:
                # YTD return (from beginning of current year)
                year_start = datetime(datetime.now().year, 1, 1)
                hist_ytd = ticker.history(start=year_start)
                if not hist_ytd.empty:
                    ytd_return = ((current_price - hist_ytd['Close'].iloc[0]) / hist_ytd['Close'].iloc[0]) * 100
                else:
                    ytd_return = 0
            except:
                ytd_return = 0
            
            # 1-year return
            try:
                one_year_ago = datetime.now() - timedelta(days=365)
                hist_1y = ticker.history(start=one_year_ago)
                if not hist_1y.empty and len(hist_1y) > 1:
                    year_return = ((current_price - hist_1y['Close'].iloc[0]) / hist_1y['Close'].iloc[0]) * 100
                else:
                    year_return = ytd_return
            except:
                year_return = ytd_return
            
            # Get volume
            volume = int(hist['Volume'].iloc[-1])
            
            # Get info
            try:
                info = ticker.info
                name = info.get('longName', info.get('shortName', f"{symbol} ETF"))
            except:
                name = f"{symbol} ETF"
            
            return {
                'symbol': symbol,
                'name': name,
                'price': float(current_price),
                'ma20': float(ma20),
                'ma50': float(ma50),
                'returnRate': float(ytd_return),
                'yearReturn': float(year_return),
                'volume': volume,
                'belowMA50': bool(current_price < ma50),
                'belowMA20': bool(current_price < ma20),
                'changePercent': float(((current_price - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100) if len(hist) > 1 else 0
            }
        
        except Exception as e:
            if attempt < retries - 1:
                logger.warning(f"Attempt {attempt + 1} failed for {symbol}: {str(e)}")
                continue
            else:
                logger.error(f"All retries failed for {symbol}: {str(e)}")
                return None
    
    return None


@app.route('/api/etfs', methods=['GET'])
def get_etfs():
    """Fetch data for all ETFs"""
    logger.info("Starting ETF data fetch...")
    
    # Use curated list of top 100 ETFs (more reliable than scraping)
    etf_symbols = get_fallback_etfs()
    
    logger.info(f"Fetching detailed data for {len(etf_symbols)} ETFs from Yahoo Finance...")
    
    etf_data = []
    
    # Use ThreadPoolExecutor for parallel fetching with reduced workers to avoid rate limiting
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_symbol = {
            executor.submit(fetch_etf_data_from_yfinance, symbol): symbol 
            for symbol in etf_symbols
        }
        
        for future in as_completed(future_to_symbol):
            symbol = future_to_symbol[future]
            try:
                data = future.result()
                if data:
                    etf_data.append(data)
                    logger.info(f"✓ {symbol}")
                else:
                    logger.warning(f"✗ {symbol}: No data returned")
            except Exception as e:
                logger.error(f"✗ {symbol}: {str(e)}")
            
            # Small delay between processing results to avoid overwhelming API
            time.sleep(0.1)
    
    logger.info(f"Successfully fetched data for {len(etf_data)} ETFs")
    
    return jsonify({
        'success': True,
        'count': len(etf_data),
        'data': etf_data,
        'timestamp': datetime.now().isoformat(),
        'source': 'ETFdb.com + Yahoo Finance'
    })


@app.route('/api/etf/<symbol>', methods=['GET'])
def get_single_etf(symbol):
    """Fetch data for a single ETF"""
    logger.info(f"Fetching data for {symbol}")
    
    data = fetch_etf_data_from_yfinance(symbol.upper())
    
    if data:
        return jsonify({
            'success': True,
            'data': data,
            'timestamp': datetime.now().isoformat()
        })
    else:
        return jsonify({
            'success': False,
            'error': f'Could not fetch data for {symbol}'
        }), 404


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'source': 'ETFdb.com + Yahoo Finance'
    })


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))
    
    print("=" * 60)
    print("ETF Data API Server")
    print("=" * 60)
    print("Data Sources: ETFdb.com + Yahoo Finance")
    print(f"Server starting on port {port}")
    print()
    print("API Endpoints:")
    print("  - GET /api/etfs        - Fetch all ETF data")
    print("  - GET /api/etf/<symbol> - Fetch single ETF data")
    print("  - GET /api/health      - Health check")
    print("=" * 60)
    print()
    app.run(debug=False, host='0.0.0.0', port=port)
