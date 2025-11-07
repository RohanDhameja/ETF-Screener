# 🚀 Deployment Guide - GitHub Pages + Render

This guide will help you deploy your ETF Screener with the frontend on **GitHub Pages** and the backend API on **Render.com** (free).

## 📋 Architecture

- **Frontend** (HTML/JS): GitHub Pages → `https://rohandhameja.github.io/ETF-Screener`
- **Backend** (Python Flask): Render.com → `https://etf-screener-api.onrender.com`

---

## Part 1: Deploy Backend to Render.com (Free)

### Step 1: Create Render Account

1. Go to [https://render.com](https://render.com)
2. Sign up with your GitHub account

### Step 2: Deploy the Backend

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository: `RohanDhameja/ETF-Screener`
3. Configure:
   - **Name**: `etf-screener-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python etf_api.py`
   - **Plan**: `Free`

4. Click **"Create Web Service"**

5. Wait 5-10 minutes for deployment. You'll get a URL like:
   `https://etf-screener-api.onrender.com`

### Step 3: Test Your API

Visit: `https://etf-screener-api.onrender.com/api/health`

You should see:
```json
{
  "status": "healthy",
  "timestamp": "...",
  "source": "ETFdb.com + Yahoo Finance"
}
```

### Step 4: Update Frontend API URL

In `etf-screener.html`, update line 245 with your actual Render URL:

```javascript
const API_URL = window.location.hostname === 'rohandhameja.github.io' 
    ? 'https://YOUR-APP-NAME.onrender.com'  // Replace with your actual URL
    : 'http://localhost:8000';
```

---

## Part 2: Deploy Frontend to GitHub Pages

### Step 1: Push Your Changes

```bash
cd "/Users/rhuria/ETF search"
git add .
git commit -m "Configure for GitHub Pages deployment"
git push origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository: [https://github.com/RohanDhameja/ETF-Screener](https://github.com/RohanDhameja/ETF-Screener)
2. Click **Settings** → **Pages** (left sidebar)
3. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/ (root)`
4. Click **Save**

### Step 3: Wait for Deployment

- GitHub will take 1-2 minutes to build and deploy
- Your site will be live at: `https://rohandhameja.github.io/ETF-Screener`

### Step 4: Access Your Site

Visit: **https://rohandhameja.github.io/ETF-Screener/etf-screener.html**

---

## 🎉 You're Live!

Your ETF Screener is now deployed:
- **Frontend**: https://rohandhameja.github.io/ETF-Screener/etf-screener.html
- **Backend API**: https://your-app.onrender.com

---

## 🔧 Troubleshooting

### Issue: CORS Errors

If you see CORS errors in the browser console, the Flask backend is already configured with `flask-cors`. Make sure your Render deployment is using the latest code.

### Issue: API Loading Slowly

Render's free tier has a "cold start" - the first request after 15 minutes of inactivity takes ~30 seconds. Subsequent requests are fast.

### Issue: 403 Forbidden

Make sure your repository is **Public** in GitHub settings.

---

## 💡 Pro Tips

1. **Custom Domain**: You can add a custom domain in GitHub Pages settings
2. **Rename File**: Rename `etf-screener.html` to `index.html` so your URL becomes just:
   `https://rohandhameja.github.io/ETF-Screener/`
3. **Keep Backend Awake**: Use a service like [UptimeRobot](https://uptimerobot.com) to ping your API every 5 minutes to prevent cold starts

---

## 🔄 Updating Your Site

After making changes:

```bash
cd "/Users/rhuria/ETF search"
git add .
git commit -m "Your update message"
git push origin main
```

Both GitHub Pages and Render will automatically redeploy!

---

## 📊 Monitoring

- **Render Dashboard**: Check logs and status at [https://dashboard.render.com](https://dashboard.render.com)
- **GitHub Pages**: Check deployment status in your repo's **Actions** tab

---

## Alternative: Railway.app (Also Free)

If Render doesn't work, try Railway:

1. Go to [https://railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repository
5. Railway will auto-detect Python and deploy
6. Update your frontend API URL with the Railway URL

---

## ⚠️ Important Notes

- **Free Tier Limits**:
  - Render: 750 hours/month (enough for 24/7)
  - GitHub Pages: 100GB bandwidth/month
  - Both are sufficient for personal projects

- **Cold Starts**: First request after inactivity takes 30s on free tier

- **Data**: All data is fetched live from Yahoo Finance (no database needed)

