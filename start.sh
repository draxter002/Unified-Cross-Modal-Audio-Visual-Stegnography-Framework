#!/usr/bin/env bash
# Quick start script for Unix-like systems (Linux/Mac)

echo "🔒 Steganography Framework - Quick Start"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

echo "✓ Python 3 installed"

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate venv
source .venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "🌐 Starting web server..."
echo "   Visit: http://localhost:8000"
echo ""
echo "   Press Ctrl+C to stop"
echo ""

# Start the server
python app.py
