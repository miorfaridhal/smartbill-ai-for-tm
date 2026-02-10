#!/bin/bash

echo "========================================="
echo "  SmartBill AI - TM Bill Analyzer"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python3 found: $(python3 --version)"
echo ""

# Check if streamlit is installed
if ! python3 -c "import streamlit" &> /dev/null
then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

echo "🚀 Starting SmartBill AI..."
echo "📱 The app will open in your browser automatically"
echo "🌐 Or navigate to: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the Streamlit app
streamlit run smartbill_app.py
