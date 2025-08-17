# YouTube Live Stream Viewer Bot 🤖

A sophisticated bot that simulates multiple viewers watching your YouTube live streams, designed for 24/7 operation on cloud hosting platforms.

## ✨ Features

- **Multiple Concurrent Viewers**: Support for 1-50+ simultaneous viewers
- **Realistic Behavior**: Human-like interactions (scrolling, pausing, volume changes)
- **Anti-Detection**: Separate browser profiles, staggered timing, varied user agents
- **Auto-Recovery**: Automatic restarts and error handling
- **24/7 Operation**: Designed for continuous hosting
- **Easy Deployment**: Ready for Render, Railway, Heroku, and Docker

## 🚀 Quick Deploy to Render (Free)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. **Fork this repository**
2. **Connect to Render**: 
   - Go to [render.com](https://render.com)
   - Connect your GitHub account
   - Select this repository
3. **Configure Environment Variables**:
   - `STREAM_URL`: Your YouTube live stream URL
   - `VIEWER_COUNT`: Number of viewers (start with 3-5 for free tier)
   - `RESTART_INTERVAL_HOURS`: How often to restart (4-6 hours)
4. **Deploy**: Click "Create Web Service"

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `STREAM_URL` | Your YouTube live stream URL | **Required** | `https://www.youtube.com/watch?v=abc123` |
| `VIEWER_COUNT` | Number of concurrent viewers | 5 | 10 |
| `MAX_DURATION_MINUTES` | Max session duration (0=unlimited) | 0 | 360 |
| `RESTART_INTERVAL_HOURS` | Hours between restarts | 6 | 4 |

### Resource Requirements

| Viewers | RAM | CPU | Recommended Plan |
|---------|-----|-----|------------------|
| 1-5     | 512MB | 0.1 CPU | Render Free |
| 6-15    | 1GB | 0.5 CPU | Render Starter ($7/mo) |
| 16-30   | 2GB | 1.0 CPU | Render Standard ($25/mo) |
| 31-50   | 4GB | 2.0 CPU | Render Pro ($85/mo) |

## 🛠️ Local Development

### Prerequisites
- Python 3.9+
- Chrome browser

### Installation
```bash
git clone https://github.com/yourusername/youtube-viewer-bot.git
cd youtube-viewer-bot
pip install -r requirements.txt
```

### Configuration
```bash
cp config.env .env
# Edit .env with your stream URL
```

### Run
```bash
python main.py
```

## 📊 Usage Examples

### Single Video Viewing
```python
from youtube_viewer import YouTubeViewer

viewer = YouTubeViewer()
await viewer.setup_browser()
await viewer.watch_video("https://www.youtube.com/watch?v=VIDEO_ID")
```

### Live Stream Viewing
```python
from live_stream_viewer import MultiViewerManager

manager = MultiViewerManager()
await manager.create_viewers(
    count=10,
    stream_url="https://www.youtube.com/watch?v=STREAM_ID",
    max_duration_minutes=60
)
```

## 🔧 Advanced Features

### Profile Management
```bash
python manage_profiles.py
```

### Testing
```bash
python test_viewers.py
python test_profiles.py
```

## 🌐 Deployment Options

### Render (Recommended for Free Tier)
- ✅ Free tier: 750 hours/month
- ✅ Automatic deployments
- ✅ Chrome support
- ✅ Easy setup

### Railway
- ✅ $5/month hobby plan
- ✅ Excellent performance
- ✅ Simple deployment

### Heroku
- ✅ Reliable platform
- ❌ No free tier
- ✅ Chrome buildpack available

### Docker
```bash
docker-compose up -d
```

## 📈 Monitoring

The bot provides detailed logging:
- Viewer connection status
- Stream availability checks
- Error handling and recovery
- Performance metrics

Check logs in your hosting platform's dashboard or `viewer_bot.log` locally.

## ⚠️ Important Notes

### Legal & Ethical Use
- Use responsibly within YouTube's Terms of Service
- Don't abuse with excessive viewer counts
- Consider impact on content creators and platform

### Detection Avoidance
- Uses multiple anti-detection techniques
- Separate browser profiles for each viewer
- Realistic human behavior simulation
- Staggered timing and varied patterns

### Performance Tips
1. Start with fewer viewers (3-5) and scale up
2. Monitor resource usage on your hosting platform
3. Use restart intervals to prevent memory leaks
4. Check YouTube Studio for accurate analytics

## 🐛 Troubleshooting

### Common Issues

**"Chrome can't read profile directory"**
- Solution: Bot automatically uses temp directories on hosting platforms

**"Stream not found"**
- Verify your STREAM_URL is correct
- Ensure the stream is actually live

**Low viewer count showing**
- YouTube viewer count updates every 1-2 minutes
- Check YouTube Studio Analytics for accurate data
- Some fluctuation is normal

**Memory/Resource issues**
- Reduce VIEWER_COUNT
- Increase RESTART_INTERVAL_HOURS
- Upgrade hosting plan

## 📞 Support

If you encounter issues:
1. Check the application logs
2. Verify your configuration
3. Test with fewer viewers
4. Ensure your stream is live
5. Check hosting platform status

## 📄 License

This project is for educational purposes. Use responsibly and in accordance with YouTube's Terms of Service.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**⭐ Star this repository if it helped you!**