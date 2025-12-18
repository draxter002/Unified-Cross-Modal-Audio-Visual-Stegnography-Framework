# Quick Setup Script for Deployment
# Run this to prepare your project for deployment

Write-Host "🔒 Steganography Framework - Deployment Setup" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git is not installed. Please install Git first:" -ForegroundColor Red
    Write-Host "   https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

Write-Host "✓ Git is installed" -ForegroundColor Green

# Check if Python is installed
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed. Please install Python first:" -ForegroundColor Red
    Write-Host "   https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

Write-Host "✓ Python is installed" -ForegroundColor Green
Write-Host ""

# Initialize git repository
Write-Host "📦 Initializing Git repository..." -ForegroundColor Cyan
if (!(Test-Path .git)) {
    git init
    Write-Host "✓ Git repository initialized" -ForegroundColor Green
} else {
    Write-Host "✓ Git repository already exists" -ForegroundColor Green
}

# Create .gitignore if it doesn't exist
if (!(Test-Path .gitignore)) {
    Write-Host "⚠️  Creating .gitignore..." -ForegroundColor Yellow
    @"
__pycache__/
*.py[cod]
.venv/
*.log
steg_uploads/
.env
"@ | Out-File -FilePath .gitignore -Encoding UTF8
    Write-Host "✓ .gitignore created" -ForegroundColor Green
}

Write-Host ""
Write-Host "📋 Next Steps:" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Test locally:" -ForegroundColor White
Write-Host "   python app.py" -ForegroundColor Yellow
Write-Host "   Then open: http://localhost:8000" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Create GitHub repository:" -ForegroundColor White
Write-Host "   - Go to https://github.com/new" -ForegroundColor Gray
Write-Host "   - Create a new public repository" -ForegroundColor Gray
Write-Host "   - Don't initialize with README (we have one)" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Push to GitHub:" -ForegroundColor White
Write-Host "   git add ." -ForegroundColor Yellow
Write-Host '   git commit -m "Initial commit"' -ForegroundColor Yellow
Write-Host "   git remote add origin YOUR_GITHUB_URL" -ForegroundColor Yellow
Write-Host "   git branch -M main" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "4. Deploy for FREE:" -ForegroundColor White
Write-Host ""
Write-Host "   Option A - Render.com (Recommended):" -ForegroundColor Magenta
Write-Host "   • Go to https://render.com" -ForegroundColor Gray
Write-Host "   • New Web Service → Connect GitHub repo" -ForegroundColor Gray
Write-Host "   • Render auto-detects settings → Deploy!" -ForegroundColor Gray
Write-Host "   • Free domain: https://your-app.onrender.com" -ForegroundColor Gray
Write-Host ""
Write-Host "   Option B - Fly.io:" -ForegroundColor Magenta
Write-Host "   • Install CLI: iwr https://fly.io/install.ps1 -useb | iex" -ForegroundColor Gray
Write-Host "   • Run: fly launch" -ForegroundColor Gray
Write-Host "   • Run: fly deploy" -ForegroundColor Gray
Write-Host ""
Write-Host "   Option C - Railway.app:" -ForegroundColor Magenta
Write-Host "   • Go to https://railway.app" -ForegroundColor Gray
Write-Host "   • New Project → Deploy from GitHub" -ForegroundColor Gray
Write-Host ""
Write-Host "📖 For detailed instructions, see: DEPLOYMENT.md" -ForegroundColor Cyan
Write-Host ""
Write-Host "✅ Setup complete! Ready to deploy." -ForegroundColor Green
