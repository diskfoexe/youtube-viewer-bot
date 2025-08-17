import asyncio
from live_stream_viewer import MultiViewerManager

async def test_viewers():
    """Test script to debug viewer count issues"""
    
    # Configuration for testing
    STREAM_URL = "https://www.youtube.com/watch?v=jNXdN87sF4I"  # Replace with your stream
    VIEWER_COUNT = 3  # Start small for testing
    MAX_DURATION_MINUTES = 10  # Short test duration
    
    print("🧪 VIEWER COUNT TEST")
    print("=" * 50)
    print(f"Stream URL: {STREAM_URL}")
    print(f"Viewers to create: {VIEWER_COUNT}")
    print(f"Test duration: {MAX_DURATION_MINUTES} minutes")
    print()
    
    print("📋 TROUBLESHOOTING CHECKLIST:")
    print("✓ Make sure your stream is actually live")
    print("✓ Replace YOUR_LIVE_STREAM_ID with your real stream ID")
    print("✓ YouTube viewer count updates every 1-2 minutes")
    print("✓ It may take 5-10 minutes to see accurate counts")
    print("✓ Check that viewers are using different browser profiles")
    print()
    
    # Confirm before starting
    response = input("Ready to start test? (y/n): ")
    if response.lower() != 'y':
        print("Test cancelled")
        return
    
    manager = MultiViewerManager()
    
    try:
        print(f"\n🚀 Starting {VIEWER_COUNT} viewers...")
        print("Watch your YouTube Studio or stream dashboard for viewer count changes")
        print("This may take 5-10 minutes to show accurate results")
        print()
        
        await manager.create_viewers(VIEWER_COUNT, STREAM_URL, MAX_DURATION_MINUTES)
        
        print("\n✅ Test completed!")
        print("\n📊 WHAT TO CHECK:")
        print("1. Did you see viewer count increase in YouTube Studio?")
        print("2. Did all viewers show 'Connection verified' messages?")
        print("3. Were there any error messages above?")
        print("\n💡 TIPS:")
        print("- If count didn't increase, try waiting 5-10 more minutes")
        print("- Check YouTube Studio Analytics for more detailed viewer data")
        print("- Try running with fewer viewers first (2-3)")
        
    except KeyboardInterrupt:
        print("\n⏹️ Test interrupted by user")
        await manager.stop_all_viewers()
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")

if __name__ == "__main__":
    asyncio.run(test_viewers())