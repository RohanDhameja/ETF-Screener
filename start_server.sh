#!/bin/bash

echo "=========================================="
echo "ETF Screener - Setup & Start"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✓ Python 3 is installed"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 first."
    exit 1
fi

echo "✓ pip3 is installed"
echo ""

# Install dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "✓ Dependencies installed successfully"
echo ""
echo "=========================================="
echo "Starting ETF API Server..."
echo "=========================================="
echo ""
echo "The server will start on http://localhost:5000"
echo ""
echo "Next steps:"
echo "1. Wait for the server to start (you'll see 'Running on http://0.0.0.0:5000')"
echo "2. Open etf-screener.html in your browser"
echo "3. Click 'Load ETF Data' button"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "=========================================="
echo ""

# Start the Flask server
python3 etf_api.py

