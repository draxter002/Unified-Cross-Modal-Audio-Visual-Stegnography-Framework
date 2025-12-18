# 🚀 Deployment Guide - Free Hosting Options

This guide shows you how to deploy your Steganography Framework to the web for **FREE** with a custom domain.

## Quick Overview

Your project is now ready to deploy as a web application! I've created:
- ✅ `app.py` - FastAPI web server with REST API
- ✅ `static/index.html` - Beautiful web interface
- ✅ Deployment configs for multiple platforms

## 🌐 Free Hosting Options

### Option 1: Render.com (Recommended - Easiest)

**Free tier includes:**
- Free subdomain: `your-app.onrender.com`
- Custom domain support (bring your own)
- Automatic HTTPS
- 750 hours/month free

**Steps:**

1. **Create a GitHub repository** (if you haven't already):
   ```powershell
   cd "C:\Users\paula\OneDrive\Desktop\coding\projects\Unified Cross Modal Audio-Visual Steganography Framework"
   git init
   git add .
   git commit -m "Initial commit with web deployment"
   ```

2. **Push to GitHub:**
   ```powershell
   # Create repo on GitHub, then:
   git remote add origin https://github.com/YOUR_USERNAME/steganography-app.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Render:**
   - Go to https://render.com and sign up (free)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect settings from `Procfile`
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment

4. **Get your free domain:**
   - Your app will be live at: `https://your-app-name.onrender.com`
   - To add a custom domain: Dashboard → Settings → Custom Domain

### Option 2: Fly.io (Best Performance)

**Free tier includes:**
- 3 shared-cpu VMs
- 3GB persistent storage
- Custom domains included
- Global edge network

**Steps:**

1. **Install Fly CLI:**
   ```powershell
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   ```

2. **Sign up and authenticate:**
   ```powershell
   fly auth signup
   # or if you have an account:
   fly auth login
   ```

3. **Launch your app:**
   ```powershell
   cd "C:\Users\paula\OneDrive\Desktop\coding\projects\Unified Cross Modal Audio-Visual Steganography Framework"
   fly launch
   ```
   - Follow prompts (I've already created `fly.toml` for you)
   - Choose a region close to you
   - Don't add PostgreSQL when asked

4. **Deploy:**
   ```powershell
   fly deploy
   ```

5. **Get your URL:**
   ```powershell
   fly status
   ```
   Your app will be at: `https://your-app-name.fly.dev`

6. **Add custom domain:**
   ```powershell
   fly domains add yourdomain.com
   ```

### Option 3: Railway.app (Fastest Setup)

**Free tier includes:**
- $5 credit per month (enough for small apps)
- Custom domains
- Automatic deployments

**Steps:**

1. **Sign up:** Go to https://railway.app
2. **New Project** → "Deploy from GitHub repo"
3. Connect your repo
4. Railway auto-detects Dockerfile
5. Deploy!

Your app will be at: `https://your-app.railway.app`

### Option 4: Vercel (For Lightweight Usage)

**Note:** Vercel is better for static sites, but can work for lightweight APIs.

**Steps:**

1. **Install Vercel CLI:**
   ```powershell
   npm install -g vercel
   ```

2. **Deploy:**
   ```powershell
   cd "C:\Users\paula\OneDrive\Desktop\coding\projects\Unified Cross Modal Audio-Visual Steganography Framework"
   vercel
   ```

3. Follow prompts and deploy!

## 🎯 Recommended: Render.com

**For your use case, I recommend Render.com because:**
- ✅ Completely free (no credit card needed)
- ✅ Easy GitHub integration
- ✅ Automatic deployments on push
- ✅ Custom domain support
- ✅ Persistent storage for temp files
- ✅ Great uptime

## 📝 Free Domain Options

If you don't have a domain, here are free options:

1. **Freenom** (freenom.com) - Free domains: .tk, .ml, .ga, .cf, .gq
2. **Afraid.org** - Free subdomains
3. **InfinityFree** - Free hosting + subdomain
4. **Use platform subdomain** - All platforms give you one for free!

## 🔧 Testing Locally First

Before deploying, test the app locally:

```powershell
# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Then visit: `http://localhost:8000`

## 🚀 Quick Start Commands (Render.com)

```powershell
# 1. Initialize git
cd "C:\Users\paula\OneDrive\Desktop\coding\projects\Unified Cross Modal Audio-Visual Steganography Framework"
git init
git add .
git commit -m "Initial deployment setup"

# 2. Create GitHub repo (do this on github.com)
# Then add remote:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main

# 3. Go to render.com
#    - Sign up
#    - New Web Service
#    - Connect GitHub repo
#    - Deploy!
```

## 📊 What Each File Does

- `app.py` - Main FastAPI application (API endpoints)
- `static/index.html` - Web interface (frontend)
- `Procfile` - Tells Render how to run the app
- `Dockerfile` - Container config for Fly/Railway
- `fly.toml` - Fly.io configuration
- `vercel.json` - Vercel configuration
- `runtime.txt` - Python version specification
- `requirements.txt` - Updated with web dependencies

## 🔒 Security Notes

1. **Environment Variables:** If you add any secrets later, use platform-specific env vars (don't commit to git)
2. **CORS:** Currently allows all origins - restrict this in production
3. **Rate Limiting:** Consider adding rate limiting for production
4. **File Size Limits:** Currently unlimited - add limits for production

## 🎨 Customization

### Change the app name in fly.toml:
```toml
app = "your-custom-name"
```

### Update CORS in app.py (line 29):
```python
allow_origins=["https://yourdomain.com"]
```

## 📞 Support

If you encounter issues:
1. Check platform status pages
2. Review deployment logs on platform dashboard
3. Test locally first with `python app.py`

## 🎉 Next Steps After Deployment

1. ✅ Test all features on the live site
2. ✅ Add your custom domain
3. ✅ Share the link with others!
4. ✅ (Optional) Add GitHub Actions for automated testing
5. ✅ (Optional) Add analytics

---

**Your app is ready to deploy! Choose a platform above and follow the steps. I recommend starting with Render.com for the easiest experience.**
