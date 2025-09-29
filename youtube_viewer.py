import asyncio
import random
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from selenium_driverless.types.webelement import WebElement
import time
import os

class YouTubeViewer:
    def __init__(self):
        self.driver = None
        
    async def setup_browser(self):
        """Initialize the driverless browser with stealth settings"""
        options = webdriver.ChromeOptions()

        # Required arguments for headless, sandboxed environments like Render
        options.add_argument("--headless=new")  # Use new headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--remote-debugging-port=9222")  # Optional but helps with some setups
        options.add_argument("--no-first-run")
        options.add_argument("--disable-infobars")
        
        # Use the manually downloaded Chrome binary path from your render-build.sh
        chrome_binary_path = "/opt/render/project/.render/chrome/opt/google/chrome/google-chrome"
        if not os.path.exists(chrome_binary_path):
            raise FileNotFoundError(f"Chrome binary not found at {chrome_binary_path}")
        options.binary_location = chrome_binary_path

        # Initialize the browser
        self.driver = await webdriver.Chrome(options=options)
        
    async def human_delay(self, min_seconds=1, max_seconds=3):
        """Add human-like random delays"""
        delay = random.uniform(min_seconds, max_seconds)
        await asyncio.sleep(delay)
    
    async def is_video_playing(self):
        """Check if video is currently playing"""
        try:
            video_info = await self.driver.execute_script("""
                const video = document.querySelector('video');
                if (!video) return {exists: false};
                return {
                    exists: true,
                    paused: video.paused,
                    ended: video.ended,
                    readyState: video.readyState,
                    currentTime: video.currentTime,
                    duration: video.duration
                };
            """)
            
            if video_info and video_info.get('exists'):
                print(f"Video status: paused={video_info.get('paused')}, ended={video_info.get('ended')}, readyState={video_info.get('readyState')}, time={video_info.get('currentTime'):.1f}s")
                return not video_info.get('paused') and not video_info.get('ended') and video_info.get('readyState', 0) > 2
            else:
                print("No video element found")
                return False
        except Exception as e:
            print(f"Error checking video status: {e}")
            return False
        
    async def handle_youtube_overlays(self):
        """Handle common YouTube overlays that might block video playback"""
        try:
            # Handle age verification
            age_gate_selectors = [
                "button[aria-label*='confirm']",
                "button[aria-label*='Continue']", 
                "#confirm-button",
                ".style-scope.ytd-button-renderer[aria-label*='I understand']"
            ]
            
            for selector in age_gate_selectors:
                try:
                    button = await self.driver.find_element(By.CSS_SELECTOR, selector)
                    await button.click()
                    print(f"Clicked age verification: {selector}")
                    await self.human_delay(2, 3)
                    return True
                except:
                    continue
                    
            # Handle sign-in prompts
            signin_selectors = [
                "button[aria-label*='No thanks']",
                "button[aria-label*='Skip']",
                ".yt-spec-button-shape-next--size-m[aria-label*='No thanks']"
            ]
            
            for selector in signin_selectors:
                try:
                    button = await self.driver.find_element(By.CSS_SELECTOR, selector)
                    await button.click()
                    print(f"Dismissed sign-in prompt: {selector}")
                    await self.human_delay(2, 3)
                    return True
                except:
                    continue
                    
        except Exception as e:
            print(f"Error handling overlays: {e}")
        
        return False
    
    async def scroll_randomly(self):
        """Simulate human-like scrolling behavior"""
        for _ in range(random.randint(2, 5)):
            scroll_amount = random.randint(100, 400)
            await self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            await self.human_delay(0.5, 1.5)
            
    async def is_youtube_short(self, url):
        """Check if the URL is a YouTube Short"""
        return "/shorts/" in url
    
    async def watch_short(self, short_url, watch_duration_seconds=None):
        """Watch a YouTube Short with appropriate behavior"""
        print(f"Starting to watch Short: {short_url}")
        
        try:
            # Navigate to short
            await self.driver.get(short_url)
            await self.human_delay(3, 5)
            
            # Check if page loaded successfully
            page_title = await self.driver.title
            if "YouTube" not in page_title:
                print(f"❌ Failed to load Short - Invalid page title: {page_title}")
                return False
            
            # Handle overlays
            await self.handle_youtube_overlays()
            
            # Check if video element exists
            video_exists = await self.driver.execute_script("return !!document.querySelector('video');")
            if not video_exists:
                print("❌ Failed to load Short - No video element found")
                return False
            
            # Shorts usually autoplay, just wait and scroll occasionally
            if not watch_duration_seconds:
                watch_duration_seconds = random.uniform(15, 45)  # Shorts are typically 15-60 seconds
            
            print(f"✅ Short loaded successfully! Watching for {watch_duration_seconds:.1f} seconds...")
            
            # Simulate watching behavior for shorts
            intervals = random.randint(2, 4)
            interval_time = watch_duration_seconds / intervals
            
            for i in range(intervals):
                await asyncio.sleep(interval_time)
                
                # Occasionally scroll (shorts are vertical)
                if random.random() < 0.4:  # 40% chance
                    scroll_amount = random.randint(50, 200)
                    await self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                
                print(f"Watching Short... {((i+1)/intervals)*100:.0f}% complete")
            
            print("✅ Finished watching Short!")
            return True
            
        except Exception as e:
            print(f"❌ Error while watching Short: {e}")
            return False
    
    async def watch_video(self, video_url, watch_duration_minutes=None):
        """Watch a YouTube video with human-like behavior"""
        print(f"Starting to watch: {video_url}")
        
        try:
            # Navigate to video
            await self.driver.get(video_url)
            await self.human_delay(20, 30)
            # Handle cookie consent if it appears
            try:
                # Try multiple cookie button selectors
                cookie_selectors = [
                    "//button[contains(text(), 'Accept all')]",
                    "//button[contains(text(), 'I agree')]",
                    "//button[contains(text(), 'Accept')]",
                    "[aria-label*='Accept']",
                    ".VfPpkd-LgbsSe[jsname='tWT92d']"
                ]
                
                for selector in cookie_selectors:
                    try:
                        if selector.startswith("//"):
                            cookie_button = await self.driver.find_element(By.XPATH, selector)
                        else:
                            cookie_button = await self.driver.find_element(By.CSS_SELECTOR, selector)
                        
                        if cookie_button:
                            await cookie_button.click()
                            print("Accepted cookies")
                            await self.human_delay(2, 3)
                            break
                    except:
                        continue
            except:
                pass
            
            # Wait for video to load
            print("Waiting for page to load...")
            await self.human_delay(5, 8)
            
            # Check what's on the page
            page_title = await self.driver.title
            print(f"Page title: {page_title}")
            
            # Check for common failure indicators
            if "YouTube" not in page_title:
                print(f"❌ Failed to load video - Invalid page title: {page_title}")
                return False
            
            # Check for error messages
            error_indicators = await self.driver.execute_script("""
                return {
                    videoUnavailable: !!document.querySelector('[data-testid="video-unavailable"]'),
                    privateVideo: !!document.querySelector('.yt-alert-message'),
                    ageRestricted: !!document.querySelector('[data-testid="age-gate"]'),
                    deleted: document.title.includes('Video unavailable')
                };
            """)
            
            if any(error_indicators.values()):
                print(f"❌ Video cannot be played - Error indicators: {error_indicators}")
                return False
            
            # Handle any overlays first
            await self.handle_youtube_overlays()
            
            # Check if video element exists
            video_exists = await self.driver.execute_script("return !!document.querySelector('video');")
            print(f"Video element exists: {video_exists}")
            
            if not video_exists:
                print("No video element found, waiting longer...")
                await self.human_delay(5, 10)
                await self.handle_youtube_overlays()  # Try again after waiting
                video_exists = await self.driver.execute_script("return !!document.querySelector('video');")
                print(f"Video element exists after wait: {video_exists}")
                
                if not video_exists:
                    print("❌ Failed to load video - No video element found after extended wait")
                    return False
            
            print("Attempting to start video playback...")
            
            # Check initial video state
            await self.is_video_playing()
            
            # Multiple attempts to start the video
            video_started = False
            
            # Method 1: Wait for autoplay or click video area
            try:
                # First check if it's already playing
                if await self.is_video_playing():
                    print("Video is already playing!")
                    video_started = True
                else:
                    # Try clicking the video area
                    video_selectors = ["#movie_player", ".html5-video-player", "video"]
                    for selector in video_selectors:
                        try:
                            video_element = await self.driver.find_element(By.CSS_SELECTOR, selector)
                            await video_element.click()
                            print(f"Clicked video element: {selector}")
                            await self.human_delay(2, 3)
                            if await self.is_video_playing():
                                video_started = True
                                break
                        except Exception as e:
                            print(f"Failed to click {selector}: {e}")
                            continue
            except Exception as e:
                print(f"Method 1 failed: {e}")
            
            # Method 2: Try play buttons
            if not video_started:
                try:
                    play_selectors = [
                        ".ytp-large-play-button",
                        ".ytp-play-button", 
                        "button[aria-label*='Play']",
                        "[title*='Play']"
                    ]
                    
                    for selector in play_selectors:
                        try:
                            play_button = await self.driver.find_element(By.CSS_SELECTOR, selector)
                            await play_button.click()
                            print(f"Clicked play button: {selector}")
                            await self.human_delay(2, 3)
                            if await self.is_video_playing():
                                video_started = True
                                break
                        except Exception as e:
                            print(f"Failed to click {selector}: {e}")
                            continue
                except Exception as e:
                    print(f"Method 2 failed: {e}")
            
            # Method 3: JavaScript play
            if not video_started:
                try:
                    result = await self.driver.execute_script("""
                        const video = document.querySelector('video');
                        if (video) {
                            const playPromise = video.play();
                            if (playPromise !== undefined) {
                                return playPromise.then(() => 'success').catch(e => 'error: ' + e.message);
                            }
                            return 'no promise';
                        }
                        return 'no video';
                    """)
                    print(f"JavaScript play result: {result}")
                    await self.human_delay(2, 3)
                    if await self.is_video_playing():
                        video_started = True
                except Exception as e:
                    print(f"Method 3 failed: {e}")
            
            # Method 4: Keyboard spacebar
            if not video_started:
                try:
                    body = await self.driver.find_element(By.TAG_NAME, "body")
                    await body.send_keys(" ")
                    print("Pressed spacebar")
                    await self.human_delay(2, 3)
                    if await self.is_video_playing():
                        video_started = True
                except Exception as e:
                    print(f"Method 4 failed: {e}")
            
            # Final check
            await self.human_delay(2, 4)
            if await self.is_video_playing():
                print("✓ Video is now playing!")
                video_started = True
            else:
                print("⚠ Video is not playing - checking for issues...")
                
                # Debug: Check for common blocking elements
                blocking_elements = await self.driver.execute_script("""
                    const checks = {
                        ageGate: !!document.querySelector('[data-testid="age-gate"]'),
                        signInRequired: !!document.querySelector('ytd-consent-bump-v2-lightbox'),
                        adPlaying: !!document.querySelector('.ad-showing'),
                        errorMessage: !!document.querySelector('.ytp-error')
                    };
                    return checks;
                """)
                print(f"Blocking elements check: {blocking_elements}")
                
                if not video_started:
                    print("❌ Failed to start video playback after all attempts")
                    return False
            
            print("✅ Video loaded and playing successfully!")
            
            # Get video duration if not specified
            if not watch_duration_minutes:
                try:
                    duration_element = await self.driver.find_element(By.CSS_SELECTOR, ".ytp-time-duration")
                    duration_text = await duration_element.text
                    # Parse duration and watch 70-90% of it
                    watch_duration_minutes = self.parse_duration(duration_text) * random.uniform(0.7, 0.9)
                except:
                    watch_duration_minutes = random.uniform(2, 5)  # Default 2-5 minutes
            
            print(f"Watching for approximately {watch_duration_minutes:.1f} minutes...")
            
            # Simulate watching behavior
            watch_time = watch_duration_minutes * 60  # Convert to seconds
            intervals = random.randint(8, 15)  # Number of interactions during watch
            interval_time = watch_time / intervals
            
            for i in range(intervals):
                await asyncio.sleep(interval_time)
                
                # Random human-like actions
                action = random.choice(['scroll', 'pause_resume', 'volume', 'nothing'])
                
                if action == 'scroll':
                    await self.scroll_randomly()
                elif action == 'pause_resume':
                    # Occasionally pause and resume
                    if random.random() < 0.3:  # 30% chance
                        try:
                            video_player = await self.driver.find_element(By.CSS_SELECTOR, ".html5-video-player")
                            await video_player.click()  # Pause
                            await self.human_delay(2, 8)  # Pause for 2-8 seconds
                            await video_player.click()  # Resume
                        except:
                            pass
                elif action == 'volume':
                    # Occasionally adjust volume
                    if random.random() < 0.2:  # 20% chance
                        try:
                            await self.driver.execute_script("document.querySelector('video').volume = Math.random();")
                        except:
                            pass
                
                print(f"Watching... {((i+1)/intervals)*100:.0f}% complete")
            
            print("✅ Finished watching video!")
            return True
            
        except Exception as e:
            print(f"❌ Error while watching video: {e}")
            return False
    
    def parse_duration(self, duration_str):
        """Parse YouTube duration string to minutes"""
        try:
            parts = duration_str.split(':')
            if len(parts) == 2:  # MM:SS
                return int(parts[0]) + int(parts[1])/60
            elif len(parts) == 3:  # HH:MM:SS
                return int(parts[0])*60 + int(parts[1]) + int(parts[2])/60
        except:
            pass
        return 3  # Default 3 minutes if parsing fails
    
    async def close(self):
        """Close the browser"""
        if self.driver:
            await self.driver.quit()

async def main():
    viewer = YouTubeViewer()
    
    # Import video lists
    try:
        from video_lists import REGULAR_VIDEOS, YOUTUBE_SHORTS, MIXED_PLAYLIST
        
        # Choose which playlist to use
        video_urls = REGULAR_VIDEOS  # Change this to YOUTUBE_SHORTS, MIXED_PLAYLIST, etc.
        
        # Or create a custom list here
        # video_urls = [
        #     "https://www.youtube.com/watch?v=wx4h9KKcFtE",
        #     "https://www.youtube.com/shorts/SOME_SHORT_ID",
        #     # Add more URLs...
        # ]
        
    except ImportError:
        # Fallback if video_lists.py doesn't exist
        video_urls = [
            "https://www.youtube.com/watch?v=wx4h9KKcFtE",
        ]
    
    try:
        await viewer.setup_browser()
        
        print(f"Starting to watch {len(video_urls)} videos...")
        
        # Track statistics
        successful_videos = 0
        failed_videos = 0
        skipped_videos = []
        
        for i, video_url in enumerate(video_urls, 1):
            print(f"\n{'='*50}")
            print(f"Video {i}/{len(video_urls)}")
            print(f"{'='*50}")
            
            try:
                # Check if it's a Short or regular video
                if await viewer.is_youtube_short(video_url):
                    success = await viewer.watch_short(video_url)
                else:
                    success = await viewer.watch_video(video_url)
                
                if success:
                    successful_videos += 1
                    print(f"✅ Video {i} completed successfully")
                else:
                    failed_videos += 1
                    skipped_videos.append(video_url)
                    print(f"⏭️ Video {i} failed - skipping to next video")
                
            except Exception as e:
                failed_videos += 1
                skipped_videos.append(video_url)
                print(f"❌ Video {i} crashed with error: {e}")
                print(f"⏭️ Skipping to next video")
            
            # Random break between videos (like a real user)
            if i < len(video_urls):  # Don't wait after the last video
                break_time = random.uniform(10, 30)  # 10-30 seconds between videos
                print(f"Taking a {break_time:.1f} second break before next video...")
                await asyncio.sleep(break_time)
        
        # Final statistics
        print(f"\n{'='*60}")
        print(f"📊 FINAL STATISTICS")
        print(f"{'='*60}")
        print(f"✅ Successfully watched: {successful_videos}/{len(video_urls)} videos")
        print(f"❌ Failed/Skipped: {failed_videos}/{len(video_urls)} videos")
        
        if skipped_videos:
            print(f"\n⏭️ Skipped videos:")
            for i, url in enumerate(skipped_videos, 1):
                print(f"   {i}. {url}")
        
        if successful_videos > 0:
            print(f"\n🎉 Session completed! Watched {successful_videos} videos successfully!")
        else:
            print(f"\n⚠️ No videos were watched successfully")
        
        # Keep browser open for a bit
        await asyncio.sleep(5)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await viewer.close()

if __name__ == "__main__":
    asyncio.run(main())
