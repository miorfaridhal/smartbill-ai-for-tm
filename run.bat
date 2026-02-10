@echo off
echo =========================================
echo   SmartBill AI - TM Bill Analyzer
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Check if streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing dependencies...
    pip install -r requirements.txt
    echo.
)

echo 🚀 Starting SmartBill AI...
echo 📱 The app will open in your browser automatically
echo 🌐 Or navigate to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the Streamlit app
streamlit run smartbill_app.py

pause
