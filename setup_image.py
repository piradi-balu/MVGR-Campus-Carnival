"""
MVGR Campus Background Image Setup Helper

This script helps you properly set up the background image for the home page.
The image should be a JPG file of the MVGR college building.

Expected location: static/images/mvgr-campus.jpg
"""

import os
import sys

def setup_image_folder():
    """Ensure the image folder exists"""
    base_path = r"C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival"
    images_path = os.path.join(base_path, "static", "images")
    
    # Create directory if it doesn't exist
    os.makedirs(images_path, exist_ok=True)
    
    print("✓ Images folder ready at:")
    print(f"  {images_path}\n")
    
    # Check if image exists
    image_file = os.path.join(images_path, "mvgr-campus.jpg")
    if os.path.exists(image_file):
        size = os.path.getsize(image_file)
        print(f"✓ Image found: mvgr-campus.jpg ({size} bytes)")
        return True
    else:
        print("✗ Image not found. Please add mvgr-campus.jpg to the folder above.")
        print("\nInstructions:")
        print("1. Save your MVGR campus building image as 'mvgr-campus.jpg'")
        print("2. Place it in the folder above")
        print("3. Restart the Django server")
        print("4. Refresh your browser at http://localhost:8000/")
        return False

def check_settings():
    """Verify Django settings are configured correctly"""
    settings_path = r"C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival\campuscarnival\settings.py"
    
    with open(settings_path, 'r') as f:
        content = f.read()
        
    checks = {
        'STATICFILES_DIRS': 'STATICFILES_DIRS' in content,
        'STATIC_URL': 'STATIC_URL' in content,
    }
    
    print("\nSettings verification:")
    for key, status in checks.items():
        symbol = "✓" if status else "✗"
        print(f"  {symbol} {key}: {'OK' if status else 'MISSING'}")
    
    return all(checks.values())

def check_template():
    """Verify template is configured correctly"""
    template_path = r"C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival\student\templates\home.html"
    
    with open(template_path, 'r') as f:
        content = f.read()
    
    checks = {
        'Load Static Tag': '{% load static %}' in content,
        'Background CSS': 'background' in content,
        'Hero Section Z-index': 'z-index: 1' in content,
    }
    
    print("\nTemplate verification:")
    for key, status in checks.items():
        symbol = "✓" if status else "✗"
        print(f"  {symbol} {key}: {'OK' if status else 'MISSING'}")
    
    return all(checks.values())

if __name__ == "__main__":
    print("=" * 60)
    print("MVGR Campus Background Image Setup")
    print("=" * 60 + "\n")
    
    setup_image_folder()
    check_settings()
    check_template()
    
    print("\n" + "=" * 60)
    print("Next steps:")
    print("1. Add mvgr-campus.jpg to: static/images/")
    print("2. Restart Django server (Ctrl+C then python manage.py runserver)")
    print("3. Refresh browser: http://localhost:8000/")
    print("=" * 60)
