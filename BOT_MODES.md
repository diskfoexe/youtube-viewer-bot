# 🤖 Bot Modes Guide

Your YouTube viewer bot now supports **3 different modes**:

## 🎥 Mode 1: LIVE (Live Streams Only)
**Best for:** Live streamers who want consistent viewers during streams

**Configuration:**
```
BOT_MODE=LIVE
STREAM_URL=https://www.youtube.com/watch?v=YOUR_LIVE_STREAM_ID
VIEWER_COUNT=5
```

**How it works:**
- Connects to your live stream
- Maintains viewers throughout the stream
- Automatically detects when stream ends
- Restarts every few hours for stability

---

## 📹 Mode 2: VIDEO (Regular Videos Only)
**Best for:** Boosting views on uploaded videos

**Configuration:**
```
BOT_MODE=VIDEO
VIDEO_URLS=https://www.youtube.com/watch?v=VIDEO1,https://www.youtube.com/watch?v=VIDEO2,https://www.youtube.com/watch?v=VIDEO3
VIEWER_COUNT=5
```

**How it works:**
- Cycles through your video list
- Each viewer watches random videos from your list
- Watches 70-90% of each video (realistic behavior)
- Takes breaks between videos
- Continues 24/7 with periodic restarts

---

## 🎭 Mode 3: MIXED (Both Live Streams and Videos)
**Best for:** Content creators who do both live streams and upload videos

**Configuration:**
```
BOT_MODE=MIXED
STREAM_URL=https://www.youtube.com/watch?v=YOUR_LIVE_STREAM_ID
VIDEO_URLS=https://www.youtube.com/watch?v=VIDEO1,https://www.youtube.com/watch?v=VIDEO2
VIEWER_COUNT=5
```

**How it works:**
- Randomly switches between live stream viewing and video viewing
- When live stream is active → watches live stream
- When no live stream → watches your videos
- Perfect for creators with mixed content

---

## ⚙️ Environment Variables

| Variable | Description | Example | Required For |
|----------|-------------|---------|--------------|
| `BOT_MODE` | Which mode to run | `LIVE`, `VIDEO`, or `MIXED` | All modes |
| `STREAM_URL` | Your live stream URL | `https://www.youtube.com/watch?v=abc123` | LIVE, MIXED |
| `VIDEO_URLS` | Comma-separated video URLs | `url1,url2,url3` | VIDEO, MIXED |
| `VIEWER_COUNT` | Number of concurrent viewers | `5` | All modes |
| `RESTART_INTERVAL_HOURS` | Hours between restarts | `6` | All modes |

---

## 🚀 Render Deployment Examples

### For Live Streams:
```yaml
envVars:
  - key: BOT_MODE
    value: LIVE
  - key: STREAM_URL
    value: https://www.youtube.com/watch?v=YOUR_STREAM_ID
  - key: VIEWER_COUNT
    value: 5
```

### For Videos:
```yaml
envVars:
  - key: BOT_MODE
    value: VIDEO
  - key: VIDEO_URLS
    value: https://www.youtube.com/watch?v=vid1,https://www.youtube.com/watch?v=vid2,https://www.youtube.com/watch?v=vid3
  - key: VIEWER_COUNT
    value: 5
```

### For Mixed:
```yaml
envVars:
  - key: BOT_MODE
    value: MIXED
  - key: STREAM_URL
    value: https://www.youtube.com/watch?v=YOUR_STREAM_ID
  - key: VIDEO_URLS
    value: https://www.youtube.com/watch?v=vid1,https://www.youtube.com/watch?v=vid2
  - key: VIEWER_COUNT
    value: 5
```

---

## 📊 Performance Comparison

| Mode | Resource Usage | Best For | Viewer Behavior |
|------|----------------|----------|-----------------|
| **LIVE** | Medium | Live streamers | Continuous viewing |
| **VIDEO** | Low-Medium | Video creators | Cycles through videos |
| **MIXED** | Medium-High | Mixed creators | Adaptive behavior |

---

## 💡 Tips for Each Mode

### LIVE Mode Tips:
- Set `RESTART_INTERVAL_HOURS=6` for stability
- Monitor during your actual streams
- Check YouTube Studio for real-time analytics

### VIDEO Mode Tips:
- Add 5-10 of your best videos to `VIDEO_URLS`
- Use shorter `RESTART_INTERVAL_HOURS=4` for more variety
- Mix old and new videos for balanced growth

### MIXED Mode Tips:
- Perfect for creators who stream AND upload
- Bot automatically adapts to your content schedule
- Provides consistent engagement across all content types

---

## 🔧 Switching Modes

To change modes on Render:
1. Go to your Render dashboard
2. Click on your service
3. Go to "Environment" tab
4. Update `BOT_MODE` variable
5. Click "Save Changes"
6. Service will automatically redeploy

---

**Choose the mode that best fits your content strategy!** 🎯