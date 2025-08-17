# Live Stream Viewer Configuration

# Your live stream URL (replace with your actual stream)
STREAM_URL = "https://www.youtube.com/watch?v=QmgZJmzL-0U"

# Viewer settings
VIEWER_CONFIGS = {
    "small_test": {
        "count": 3,
        "max_duration_minutes": 30,
        "description": "Small test with 3 viewers for 30 minutes"
    },
    
    "medium_stream": {
        "count": 10,
        "max_duration_minutes": 60,
        "description": "Medium stream with 10 viewers for 1 hour"
    },
    
    "large_stream": {
        "count": 25,
        "max_duration_minutes": 120,
        "description": "Large stream with 25 viewers for 2 hours"
    },
    
    "max_stream": {
        "count": 50,
        "max_duration_minutes": None,  # Unlimited duration
        "description": "Maximum viewers (50) for unlimited time"
    }
}

# Advanced settings
ADVANCED_SETTINGS = {
    "stagger_start_max_seconds": 60,  # Max delay between viewer starts
    "behavior_frequency_seconds": (30, 120),  # Min/max time between actions
    "enable_chat_interaction": False,  # Future feature
    "enable_different_qualities": True,  # Different video qualities per viewer
    "enable_mobile_simulation": False,  # Simulate mobile viewers
}

# Resource management
RESOURCE_LIMITS = {
    "max_concurrent_browsers": 50,  # System limit
    "memory_limit_gb": 8,  # Estimated memory usage limit
    "cpu_cores_to_use": 4,  # Number of CPU cores to utilize
}