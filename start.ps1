# Quick start script for Windows
# Double-click this file to run the web app

Write-Host "🔒 Steganography Framework - Quick Start" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python installed: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python is not installed" -ForegroundColor Red
    Write-Host "   Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if venv exists
if (!(Test-Path .venv)) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Cyan
    python -m venv .venv
}

# Activate venv and install dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Cyan
& ".\.venv\Scripts\pip.exe" install -q -r requirements.txt

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Starting web server..." -ForegroundColor Cyan
Write-Host "   Visit: http://localhost:8000" -ForegroundColor Yellow
Write-Host ""
Write-Host "   Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""

# Start the server
try {
    & ".\.venv\Scripts\python.exe" app.py
} catch {
    Write-Host ""
    Write-Host "Server stopped." -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Press Enter to exit"
