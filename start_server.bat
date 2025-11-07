@echo off
echo ==========================================
echo ETF Screener - Setup ^& Start
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed. Please install Python 3 first.
    pause
    exit /b 1
)

echo √ Python is installed
echo.

REM Install dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo X Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo √ Dependencies installed successfully
echo.
echo ==========================================
echo Starting ETF API Server...
echo ==========================================
echo.
echo The server will start on http://localhost:5000
echo.
echo Next steps:
echo 1. Wait for the server to start
echo 2. Open etf-screener.html in your browser
echo 3. Click 'Load ETF Data' button
echo.
echo Press Ctrl+C to stop the server
echo.
echo ==========================================
echo.

REM Start the Flask server
python etf_api.py

