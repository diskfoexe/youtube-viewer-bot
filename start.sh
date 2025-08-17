#!/bin/bash
# Start script for YouTube Viewer Bot

echo "🚀 Starting YouTube Viewer Bot..."

# Check if config exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found. Copying from config.env..."
    cp config.env .env
    echo "📝 Please edit .env file with your stream URL before running again!"
    exit 1
fi

# Load environment variables
source .env

# Validate stream URL
if [[ "$STREAM_URL" == *"YOUR_STREAM_ID"* ]]; then
    echo "❌ Please update STREAM_URL in .env file with your actual stream URL!"
    exit 1
fi

# Create necessary directories
mkdir -p logs chrome_profiles

# Start the bot
echo "🤖 Starting bot with $VIEWER_COUNT viewers..."
echo "📺 Stream: $STREAM_URL"

python main.py