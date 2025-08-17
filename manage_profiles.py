import os
import shutil
from pathlib import Path

class ProfileManager:
    def __init__(self, base_dir="./chrome_profiles"):
        self.base_dir = Path(base_dir)
    
    def create_profiles(self, count):
        """Create profile directories for specified number of viewers"""
        print(f"📁 Creating {count} Chrome profile directories...")
        
        # Create base directory
        self.base_dir.mkdir(exist_ok=True)
        
        created = 0
        for i in range(1, count + 1):
            profile_dir = self.base_dir / f"viewer_{i}"
            
            if not profile_dir.exists():
                profile_dir.mkdir(parents=True, exist_ok=True)
                print(f"   ✅ Created: {profile_dir}")
                created += 1
            else:
                print(f"   📂 Exists: {profile_dir}")
        
        print(f"📊 Created {created} new profiles, {count - created} already existed")
        return True
    
    def list_profiles(self):
        """List all existing profile directories"""
        if not self.base_dir.exists():
            print("❌ No profile directory found")
            return []
        
        profiles = list(self.base_dir.glob("viewer_*"))
        profiles.sort()
        
        print(f"📋 Found {len(profiles)} profile directories:")
        for profile in profiles:
            size = self.get_directory_size(profile)
            print(f"   📂 {profile.name} ({size})")
        
        return profiles
    
    def clean_profiles(self, keep_count=0):
        """Clean profile directories (delete all or keep specified number)"""
        if not self.base_dir.exists():
            print("❌ No profile directory found")
            return
        
        profiles = list(self.base_dir.glob("viewer_*"))
        profiles.sort()
        
        if keep_count == 0:
            # Delete all profiles
            print(f"🗑️ Deleting all {len(profiles)} profile directories...")
            for profile in profiles:
                try:
                    shutil.rmtree(profile)
                    print(f"   ✅ Deleted: {profile.name}")
                except Exception as e:
                    print(f"   ❌ Failed to delete {profile.name}: {e}")
        else:
            # Keep only specified number
            to_delete = profiles[keep_count:]
            if to_delete:
                print(f"🗑️ Keeping {keep_count} profiles, deleting {len(to_delete)} others...")
                for profile in to_delete:
                    try:
                        shutil.rmtree(profile)
                        print(f"   ✅ Deleted: {profile.name}")
                    except Exception as e:
                        print(f"   ❌ Failed to delete {profile.name}: {e}")
            else:
                print(f"✅ Already have {len(profiles)} profiles (≤ {keep_count}), nothing to delete")
    
    def get_directory_size(self, path):
        """Get human-readable directory size"""
        try:
            total_size = sum(f.stat().st_size for f in path.rglob('*') if f.is_file())
            
            # Convert to human readable
            for unit in ['B', 'KB', 'MB', 'GB']:
                if total_size < 1024.0:
                    return f"{total_size:.1f} {unit}"
                total_size /= 1024.0
            return f"{total_size:.1f} TB"
        except:
            return "Unknown size"
    
    def reset_profile(self, viewer_id):
        """Reset a specific viewer profile"""
        profile_dir = self.base_dir / f"viewer_{viewer_id}"
        
        if profile_dir.exists():
            try:
                shutil.rmtree(profile_dir)
                profile_dir.mkdir(parents=True, exist_ok=True)
                print(f"🔄 Reset profile for viewer_{viewer_id}")
                return True
            except Exception as e:
                print(f"❌ Failed to reset viewer_{viewer_id}: {e}")
                return False
        else:
            print(f"❌ Profile viewer_{viewer_id} doesn't exist")
            return False

def main():
    """Interactive profile management"""
    manager = ProfileManager()
    
    while True:
        print("\n" + "="*50)
        print("🛠️  CHROME PROFILE MANAGER")
        print("="*50)
        print("1. Create profiles for N viewers")
        print("2. List existing profiles")
        print("3. Clean all profiles")
        print("4. Clean profiles (keep N)")
        print("5. Reset specific profile")
        print("6. Exit")
        print()
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            try:
                count = int(input("How many viewer profiles to create? "))
                manager.create_profiles(count)
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == "2":
            manager.list_profiles()
        
        elif choice == "3":
            confirm = input("⚠️ Delete ALL profiles? (y/N): ").strip().lower()
            if confirm == 'y':
                manager.clean_profiles(0)
            else:
                print("❌ Cancelled")
        
        elif choice == "4":
            try:
                keep = int(input("How many profiles to keep? "))
                manager.clean_profiles(keep)
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == "5":
            try:
                viewer_id = int(input("Which viewer ID to reset? "))
                manager.reset_profile(viewer_id)
            except ValueError:
                print("❌ Please enter a valid viewer ID")
        
        elif choice == "6":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()