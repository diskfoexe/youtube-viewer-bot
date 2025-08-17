# 🚀 GitHub + Render Deployment Instructions

## Step 1: Push to GitHub

### 1.1 Create GitHub Repository
1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name it: `youtube-viewer-bot`
4. Make it **Public** (required for Render free tier)
5. Don't initialize with README (we have our own)
6. Click "Create repository"

### 1.2 Push Your Code
Open terminal/command prompt in your project folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: YouTube viewer bot"

# Add your GitHub repository as origin (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/youtube-viewer-bot.git

# Push to GitHub
git push -u origin main
```

**If you get an error about 'main' branch, try:**
```bash
git branch -M main
git push -u origin main
```

## Step 2: Deploy to Render

### 2.1 Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Authorize Render to access your repositories

### 2.2 Create Web Service
1. Click "New +" → "Web Service"
2. Connect your `youtube-viewer-bot` repository
3. Configure the service:

**Basic Settings:**
- **Name**: `youtube-viewer-bot`
- **Region**: `Oregon (US West)` (cheapest)
- **Branch**: `main`
- **Runtime**: `Python 3`

**Build & Deploy:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python main.py`

### 2.3 Set Environment Variables
In the "Environment" section, add these variables:

| Key | Value |
|-----|-------|
| `STREAM_URL` | `https://www.youtube.com/watch?v=YOUR_ACTUAL_STREAM_ID` |
| `VIEWER_COUNT` | `3` (start small for free tier) |
| `MAX_DURATION_MINUTES` | `0` |
| `RESTART_INTERVAL_HOURS` | `4` |
| `PYTHONUNBUFFERED` | `1` |

**⚠️ IMPORTANT**: Replace `YOUR_ACTUAL_STREAM_ID` with your real YouTube stream ID!

### 2.4 Deploy
1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Check logs for "🤖 YouTube Viewer Bot starting..."

## Step 3: Monitor Your Bot

### 3.1 Check Logs
- Go to your Render dashboard
- Click on your service
- Click "Logs" tab
- Look for messages like:
  ```
  ✅ Stream is live! Starting to watch...
  Connection verified - Viewer count: X watching
  ```

### 3.2 Verify on YouTube
- Go to your YouTube Studio
- Check Analytics → Real-time
- Should see viewer count increase within 5-10 minutes

## 🔧 Troubleshooting

### Common Issues:

**1. "Build failed"**
- Check that all files are pushed to GitHub
- Verify `requirements.txt` exists
- Check Render build logs for specific errors

**2. "Application failed to start"**
- Verify `STREAM_URL` is set correctly
- Check that your stream is actually live
- Look at Render logs for error messages

**3. "No viewers showing up"**
- Wait 5-10 minutes (YouTube updates slowly)
- Check YouTube Studio Analytics instead of live count
- Verify stream is public and live

**4. "Service keeps restarting"**
- Reduce `VIEWER_COUNT` to 2-3 for free tier
- Check memory usage in Render dashboard
- Increase `RESTART_INTERVAL_HOURS`

### Free Tier Limitations:
- **750 hours/month** (about 25 days)
- **512MB RAM** (good for 3-5 viewers max)
- **Sleeps after 15 minutes** of inactivity (but auto-wakes)

### Optimization for Free Tier:
```
VIEWER_COUNT=3
RESTART_INTERVAL_HOURS=6
```

## 🎉 Success!

If everything works, you should see:
1. ✅ Render deployment successful
2. ✅ Bot logs showing "Stream is live"
3. ✅ YouTube viewer count increasing
4. ✅ 24/7 operation

Your bot is now running 24/7 on Render's free tier! 🚀

## 📈 Scaling Up

When ready to scale:
1. Upgrade to Render Starter ($7/month)
2. Increase `VIEWER_COUNT` to 10-15
3. Monitor performance and adjust

---

**Need help?** Check the logs first, then verify your configuration!