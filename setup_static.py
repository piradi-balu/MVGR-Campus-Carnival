#!/usr/bin/env python
import os
import base64
import sys

# Get the path to save the image
static_images_path = r"C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival\static\images"

# Create the directory if it doesn't exist
os.makedirs(static_images_path, exist_ok=True)

print(f"Static images path: {static_images_path}")
print("Ready to receive image file...")
print("\nTo add the MVGR campus image:")
print("1. Copy the image file to: " + static_images_path)
print("2. Rename it to: mvgr-campus.jpg")
print("\nOR download from: https://github.com/")
