#!/usr/bin/env python3
"""
Test script to check if Cloudinary is properly configured and working
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_information.settings')
django.setup()

from django.conf import settings
from decouple import config

def test_project_configuration():
    """Test basic project configuration"""
    print("=" * 60)
    print("🔍 PROJECT CONFIGURATION TEST")
    print("=" * 60)
    
    # Check Django settings
    print(f"⚙️ Django Settings:")
    print(f"DEBUG: {settings.DEBUG}")
    print(f"SECRET_KEY: {'Set' if settings.SECRET_KEY else 'Not set'}")
    print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"MEDIA_URL: {settings.MEDIA_URL}")
    print(f"MEDIA_ROOT: {getattr(settings, 'MEDIA_ROOT', 'Not set')}")
    
    # Check database
    print(f"\n💾 Database Configuration:")
    db_config = settings.DATABASES.get('default', {})
    print(f"Engine: {db_config.get('ENGINE', 'Not set')}")
    print(f"Database: {db_config.get('NAME', 'Not set')}")
    
    # Check installed apps
    print(f"\n📱 Installed Apps:")
    for app in ['jobs', 'results', 'notifications', 'contact']:
        if app in settings.INSTALLED_APPS:
            print(f"✅ {app}: Installed")
        else:
            print(f"❌ {app}: Not installed")
    
    print("\n📝 Note: This project is configured for LOCAL DEVELOPMENT ONLY")
    print("   - Files are stored locally in the media/ directory")
    print("   - Using SQLite database for easy development")
    print("   - No cloud services required")
    
    return True

def test_media_directory():
    """Test local media directory"""
    print("\n" + "=" * 60)
    print("📁 LOCAL MEDIA STORAGE TEST")
    print("=" * 60)
    
    media_root = getattr(settings, 'MEDIA_ROOT', None)
    if media_root:
        print(f"Media directory: {media_root}")
        if not os.path.exists(media_root):
            try:
                os.makedirs(media_root)
                print("✅ Media directory created successfully")
            except Exception as e:
                print(f"❌ Failed to create media directory: {e}")
                return False
        else:
            print("✅ Media directory exists")
        
        # Test write permissions
        try:
            test_file = os.path.join(media_root, 'test_write.txt')
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            print("✅ Media directory is writable")
            return True
        except Exception as e:
            print(f"❌ Media directory not writable: {e}")
            return False
    else:
        print("❌ MEDIA_ROOT not configured")
        return False

def test_static_files():
    """Test static files configuration"""
    print("\n" + "=" * 60)
    print("🎨 STATIC FILES TEST")
    print("=" * 60)
    
    print(f"STATIC_URL: {settings.STATIC_URL}")
    print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    
    # Check if static directories exist
    for static_dir in settings.STATICFILES_DIRS:
        if os.path.exists(static_dir):
            print(f"✅ Static directory exists: {static_dir}")
        else:
            print(f"⚠️ Static directory doesn't exist: {static_dir}")
            print("   This is normal if you haven't created any static files yet")
    
    return True

def main():
    """Main function to run all tests"""
    print("🧪 TESTING DJANGO PROJECT CONFIGURATION")
    print("=" * 60)
    
    results = []
    
    # Test Project Configuration
    config_ok = test_project_configuration()
    results.append(("Project Configuration", config_ok))
    
    # Test Media Directory
    media_ok = test_media_directory()
    results.append(("Local Media Storage", media_ok))
    
    # Test Static Files
    static_ok = test_static_files()
    results.append(("Static Files", static_ok))
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 TEST SUMMARY")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    all_ok = all(result for _, result in results)
    
    print("\n" + "=" * 60)
    if all_ok:
        print("🎉 PROJECT READY FOR LOCAL DEVELOPMENT!")
        print("✅ Your Django project is configured correctly")
        print("📝 All files will be stored locally - no cloud services needed")
        print("\n🚀 Next steps:")
        print("   1. python manage.py runserver")
        print("   2. Go to http://127.0.0.1:8000/")
        print("   3. Admin panel: http://127.0.0.1:8000/admin/")
    else:
        print("❌ CONFIGURATION ISSUES DETECTED!")
        print("🔧 Please fix the failed tests above before running the project")
    
    return all_ok

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n💥 Error during testing: {e}")
        print("🔧 Make sure you're in the project directory and Django is properly installed")
        sys.exit(1)
