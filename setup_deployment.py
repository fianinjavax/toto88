#!/usr/bin/env python3
"""
Setup script to verify deployment readiness for Streamlit Cloud
"""

import os
import sys
import importlib.util

def check_requirements():
    """Check if all required packages are available"""
    required_packages = [
        'streamlit', 'requests', 'numpy', 'pandas', 'plotly', 'trafilatura'
    ]
    
    missing = []
    for package in required_packages:
        if importlib.util.find_spec(package) is None:
            missing.append(package)
    
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        return False
    else:
        print("✅ All required packages are available")
        return True

def check_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'optimized_bbfs_system.py',
        'ultra_smart_bbfs.py',
        'requirements_streamlit.txt',
        '.streamlit/config.toml',
        'README.md'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print(f"❌ Missing files: {', '.join(missing)}")
        return False
    else:
        print("✅ All required files are present")
        return True

def test_imports():
    """Test if main modules can be imported"""
    try:
        from optimized_bbfs_system import get_optimized_system
        from ultra_smart_bbfs import UltraSmartBBFS
        print("✅ Core modules import successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def main():
    print("🔍 Checking deployment readiness...")
    print("=" * 50)
    
    checks = [
        ("Requirements", check_requirements),
        ("Files", check_files),
        ("Imports", test_imports)
    ]
    
    all_passed = True
    for name, check_func in checks:
        print(f"\n📋 {name}:")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 Ready for deployment to Streamlit Cloud!")
        print("\nNext steps:")
        print("1. Upload to GitHub repository")
        print("2. Deploy on share.streamlit.io")
        print("3. Use requirements_streamlit.txt for dependencies")
    else:
        print("❌ Deployment readiness check failed")
        print("Please fix the issues above before deploying")

if __name__ == "__main__":
    main()