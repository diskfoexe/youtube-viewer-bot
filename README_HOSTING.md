# YouTube Viewer Bot - Hosting Guide

## 🚀 Deployment Options

### Option 1: bot-hosting.net (Recommended)

1. **Upload Files:**
   - Upload all `.py` files
   - Upload `requirements.txt`
   - Upload `main.py` (entry point)

2. **Configuration:**
   - Set main file: `main.py`
   - Set Python version: 3.9+
   - Add environment variables:
     ```
     STREAM_URL=https://www.youtube.com/watch?v=YOUR_ACTUAL_STREAM_ID
     VIEWER_COUNT=10
     MAX_DURATION_MINUTES=0
     RESTART_INTERVAL_HOURS=6
     ```

3. **Start Bot:**
   - Click "Start" in bot-hosting.net dashboard
   - Monitor logs for viewer activity

### Option 2: Heroku

1. **Create Heroku App:**
   ```bash
   heroku create your-youtube-viewer-bot
   ```

2. **Add Buildpacks:**
   ```bash
   heroku buildpacks:add --index 1 heroku/google-chrome
   heroku buildpacks:add --index 2 heroku/python
   ```

3. **Set Config Vars:**
   ```bash
   heroku config:set STREAM_URL=https://www.youtube.com/watch?v=YOUR_STREAM_ID
   heroku config:set VIEWER_COUNT=10
   heroku config:set MAX_DURATION_MINUTES=0
   heroku config:set RESTART_INTERVAL_HOURS=6
   ```

4. **Deploy:**
   ```bash
   git add .
   git commit -m "Deploy YouTube viewer bot"
   git push heroku main
   ```

### Option 3: Railway

1. **Connect GitHub repo to Railway**
2. **Set environment variables in Railway dashboard**
3. **Deploy automatically**

### Option 4: Docker (VPS/Cloud)

1. **Build and run:**
   ```bash
   docker-compose up -d
   ```

2. **Monitor logs:**
   ```bash
   docker-compose logs -f
   ```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `STREAM_URL` | Your YouTube live stream URL | Required | `https://www.youtube.com/watch?v=abc123` |
| `VIEWER_COUNT` | Number of concurrent viewers | 5 | 10 |
| `MAX_DURATION_MINUTES` | Max session duration (0=unlimited) | 0 | 360 |
| `RESTART_INTERVAL_HOURS` | Hours between restarts | 6 | 4 |

### Resource Requirements

| Viewers | RAM | CPU | Bandwidth |
|---------|-----|-----|-----------|
| 1-5     | 1GB | 0.5 CPU | 5 Mbps |
| 6-15    | 2GB | 1.0 CPU | 15 Mbps |
| 16-30   | 4GB | 2.0 CPU | 30 Mbps |
| 31-50   | 8GB | 4.0 CPU | 50 Mbps |

## 📊 Monitoring

### Log Files
- `viewer_bot.log` - Main application logs
- Check for "Connection verified" messages
- Monitor viewer count reports

### Health Checks
The bot automatically:
- Restarts every 6 hours (configurable)
- Recovers from crashes
- Reports viewer statistics

## 🔧 Troubleshooting

### Common Issues

1. **"Chrome can't read profile directory"**
   - Solution: Bot automatically uses temp directories on hosting platforms

2. **"Stream not found"**
   - Check your STREAM_URL is correct
   - Ensure stream is actually live

3. **Low viewer count**
   - Normal fluctuation is expected
   - Check YouTube Studio for accurate analytics
   - Increase RESTART_INTERVAL_HOURS for stability

4. **Memory issues**
   - Reduce VIEWER_COUNT
   - Increase hosting plan resources

### Performance Tips

1. **Start Small:** Begin with 5-10 viewers
2. **Monitor Resources:** Watch RAM/CPU usage
3. **Stable Hosting:** Use reliable hosting platforms
4. **Regular Restarts:** Keep RESTART_INTERVAL_HOURS at 4-8 hours

## 🚨 Important Notes

### Legal & Ethical
- Use responsibly and within YouTube's Terms of Service
- Don't abuse the system with excessive viewers
- Consider the impact on content creators

### Detection Avoidance
- The bot uses multiple techniques to appear natural
- Staggered start times and realistic behavior
- Separate browser profiles for each viewer

### Hosting Platform Compatibility
- ✅ bot-hosting.net (Recommended)
- ✅ Heroku (with Chrome buildpack)
- ✅ Railway
- ✅ DigitalOcean/VPS with Docker
- ❌ Replit (Chrome restrictions)
- ❌ GitHub Codespaces (Chrome restrictions)

## 📞 Support

If you encounter issues:
1. Check the logs first
2. Verify your configuration
3. Test with fewer viewers
4. Ensure your stream is live

Good luck with your 24/7 YouTube viewer bot! 🎉