#!/usr/bin/env python3
"""
Main entry point for YouTube viewer bot
Designed for 24/7 hosting on platforms like bot-hosting.net
"""

import asyncio
import os
import sys
import signal
import logging
from datetime import datetime
from live_stream_viewer import MultiViewerManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('viewer_bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class PersistentViewerBot:
    def __init__(self):
        self.manager = None
        self.is_running = False
        self.restart_count = 0
        
        # Configuration - EDIT THESE VALUES
        self.STREAM_URL = os.getenv('STREAM_URL', "https://www.youtube.com/watch?v=YOUR_STREAM_ID")
        self.VIEWER_COUNT = int(os.getenv('VIEWER_COUNT', '5'))
        self.MAX_DURATION_MINUTES = int(os.getenv('MAX_DURATION_MINUTES', '0')) or None  # 0 = unlimited
        self.RESTART_INTERVAL_HOURS = int(os.getenv('RESTART_INTERVAL_HOURS', '6'))  # Restart every 6 hours
        
        logging.info(f"Bot configured:")
        logging.info(f"  Stream URL: {self.STREAM_URL}")
        logging.info(f"  Viewer Count: {self.VIEWER_COUNT}")
        logging.info(f"  Max Duration: {self.MAX_DURATION_MINUTES or 'Unlimited'} minutes")
        logging.info(f"  Restart Interval: {self.RESTART_INTERVAL_HOURS} hours")
    
    async def run_viewers(self):
        """Run viewers with automatic restart capability"""
        while self.is_running:
            try:
                self.restart_count += 1
                logging.info(f"🚀 Starting viewer session #{self.restart_count}")
                
                self.manager = MultiViewerManager()
                
                # Set session duration (restart interval or max duration, whichever is shorter)
                session_duration = self.RESTART_INTERVAL_HOURS * 60  # Convert to minutes
                if self.MAX_DURATION_MINUTES:
                    session_duration = min(session_duration, self.MAX_DURATION_MINUTES)
                
                logging.info(f"Session will run for {session_duration} minutes")
                
                # Start viewers
                await self.manager.create_viewers(
                    self.VIEWER_COUNT, 
                    self.STREAM_URL, 
                    session_duration
                )
                
                logging.info(f"✅ Session #{self.restart_count} completed")
                
                if self.is_running:
                    logging.info(f"⏳ Waiting 60 seconds before restart...")
                    await asyncio.sleep(60)  # Brief pause between sessions
                
            except Exception as e:
                logging.error(f"❌ Session #{self.restart_count} failed: {e}")
                if self.is_running:
                    logging.info("⏳ Waiting 5 minutes before retry...")
                    await asyncio.sleep(300)  # Wait 5 minutes on error
    
    async def start(self):
        """Start the persistent bot"""
        self.is_running = True
        logging.info("🤖 YouTube Viewer Bot starting...")
        
        # Validate configuration
        if "YOUR_STREAM_ID" in self.STREAM_URL:
            logging.error("❌ Please update STREAM_URL with your actual stream URL!")
            return
        
        try:
            await self.run_viewers()
        except KeyboardInterrupt:
            logging.info("⏹️ Bot stopped by user")
        except Exception as e:
            logging.error(f"❌ Bot crashed: {e}")
        finally:
            await self.stop()
    
    async def stop(self):
        """Stop the bot gracefully"""
        self.is_running = False
        logging.info("🛑 Stopping bot...")
        
        if self.manager:
            await self.manager.stop_all_viewers()
        
        logging.info("✅ Bot stopped")

# Global bot instance for signal handling
bot = None

def signal_handler(signum, frame):
    """Handle shutdown signals"""
    if bot:
        logging.info(f"📡 Received signal {signum}, shutting down...")
        asyncio.create_task(bot.stop())

async def main():
    """Main entry point"""
    global bot
    
    # Set up signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    bot = PersistentViewerBot()
    await bot.start()

if __name__ == "__main__":
    # Ensure event loop compatibility
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    asyncio.run(main())