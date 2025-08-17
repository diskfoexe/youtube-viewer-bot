import os
import tempfile
from pathlib import Path

def test_profile_creation():
    """Test Chrome profile directory creation and permissions"""
    print("🧪 TESTING CHROME PROFILE CREATION")
    print("=" * 50)
    
    # Test 1: Current directory approach
    print("\n1️⃣ Testing current directory approach...")
    current_dir = os.path.abspath(os.getcwd())
    test_dir1 = os.path.join(current_dir, "chrome_profiles", "test_viewer")
    test_dir1 = os.path.normpath(test_dir1)
    
    print(f"   Path: {test_dir1}")
    
    try:
        os.makedirs(test_dir1, exist_ok=True)
        
        # Test write permissions
        test_file = os.path.join(test_dir1, "test.txt")
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        
        print("   ✅ SUCCESS: Directory created and writable")
        success1 = True
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        success1 = False
    
    # Test 2: Temp directory approach
    print("\n2️⃣ Testing temp directory approach...")
    test_dir2 = os.path.join(tempfile.gettempdir(), "youtube_viewer_test")
    test_dir2 = os.path.normpath(test_dir2)
    
    print(f"   Path: {test_dir2}")
    
    try:
        os.makedirs(test_dir2, exist_ok=True)
        
        # Test write permissions
        test_file = os.path.join(test_dir2, "test.txt")
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        
        print("   ✅ SUCCESS: Directory created and writable")
        success2 = True
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        success2 = False
    
    # Test 3: User's Documents folder
    print("\n3️⃣ Testing Documents folder approach...")
    try:
        documents_path = os.path.join(os.path.expanduser("~"), "Documents", "YouTubeViewerProfiles")
        test_dir3 = os.path.join(documents_path, "test_viewer")
        test_dir3 = os.path.normpath(test_dir3)
        
        print(f"   Path: {test_dir3}")
        
        os.makedirs(test_dir3, exist_ok=True)
        
        # Test write permissions
        test_file = os.path.join(test_dir3, "test.txt")
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        
        print("   ✅ SUCCESS: Directory created and writable")
        success3 = True
    except Exception as e:
        print(f"   ❌ FAILED: {e}")
        success3 = False
    
    # Recommendations
    print("\n📋 RECOMMENDATIONS:")
    print("=" * 30)
    
    if success1:
        print("✅ Use current directory approach (default)")
        print(f"   Path: {test_dir1}")
    elif success2:
        print("✅ Use temp directory approach (fallback)")
        print(f"   Path: {test_dir2}")
    elif success3:
        print("✅ Use Documents folder approach")
        print(f"   Path: {test_dir3}")
    else:
        print("❌ All approaches failed!")
        print("   Try running as Administrator")
        print("   Or check Windows permissions")
    
    # Cleanup
    print("\n🧹 Cleaning up test directories...")
    for test_dir in [test_dir1, test_dir2, test_dir3]:
        try:
            if os.path.exists(test_dir):
                os.rmdir(test_dir)
                print(f"   Removed: {test_dir}")
        except:
            pass
    
    return success1 or success2 or success3

if __name__ == "__main__":
    test_profile_creation()
    
    print("\n" + "=" * 50)
    print("💡 If all tests failed, try:")
    print("1. Run Command Prompt as Administrator")
    print("2. Check Windows folder permissions")
    print("3. Disable antivirus temporarily")
    print("4. Use a different drive (D:, E:, etc.)")