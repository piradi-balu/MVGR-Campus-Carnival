#!/usr/bin/env python
"""
Download MVGR-like campus building image for background
This script downloads a suitable college campus image from a free source
"""

import os
import urllib.request
import urllib.error

def download_campus_image():
    """Download a campus building image"""
    
    # Path to save image
    base_path = r"C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival"
    images_dir = os.path.join(base_path, "static", "images")
    os.makedirs(images_dir, exist_ok=True)
    
    image_path = os.path.join(images_dir, "mvgr-campus.jpg")
    
    # Check if image already exists
    if os.path.exists(image_path):
        print(f"✓ Image already exists: {image_path}")
        return True
    
    print("Attempting to download campus image...")
    print("(Using free image sources)")
    
    # Multiple image sources to try
    image_urls = [
        "https://images.pexels.com/photos/3938023/pexels-photo-3938023.jpeg?auto=compress&cs=tinysrgb&w=1600",
        "https://images.pexels.com/photos/3807517/pexels-photo-3807517.jpeg?auto=compress&cs=tinysrgb&w=1600",
        "https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=1600&h=900&fit=crop",
    ]
    
    for url in image_urls:
        try:
            print(f"Trying: {url[:50]}...")
            urllib.request.urlretrieve(url, image_path)
            print(f"✓ Image downloaded successfully!")
            print(f"  Location: {image_path}")
            return True
        except (urllib.error.URLError, urllib.error.HTTPError):
            print(f"  Could not download from that source, trying next...")
            continue
        except Exception as e:
            print(f"  Error: {e}")
            continue
    
    print("\n✗ Could not download image from online sources")
    print("\nAlternative: Please manually add mvgr-campus.jpg to:")
    print(f"  {images_dir}")
    
    return False

if __name__ == "__main__":
    print("=" * 60)
    print("Campus Image Setup")
    print("=" * 60)
    print()
    
    success = download_campus_image()
    
    print()
    if success:
        print("✓ Ready! Restart Django and refresh your browser")
    else:
        print("Please manually place mvgr-campus.jpg in the static/images/ folder")
    
    print("=" * 60)
