# How to Add the MVGR Campus Background Image

## Step 1: Locate the Image Folder
The image should be placed in:
```
C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival\static\images\
```

## Step 2: Save Your Image
1. Right-click on the MVGR campus building image
2. Select "Save image as..."
3. Navigate to the folder above
4. Name it exactly: `mvgr-campus.jpg`
5. Make sure the file extension is `.jpg`

## Step 3: Refresh Your Browser
1. Open http://localhost:8000/
2. Press Ctrl+F5 to hard refresh (clears cache)
3. You should now see the MVGR building as the background!

## What the Template Expects
The home.html template is configured to use:
```
{% static "images/mvgr-campus.jpg" %}
```

This means the image file must be named exactly:
- Filename: `mvgr-campus.jpg`
- Location: `static/images/` folder
- Format: JPG or JPEG

## File Structure Should Look Like:
```
campuscarnival/
├── static/
│   ├── images/
│   │   └── mvgr-campus.jpg  ← PUT YOUR IMAGE HERE
│   └── ...
├── student/
├── manage.py
└── ...
```

## If Image Doesn't Show
1. Check filename is exactly: `mvgr-campus.jpg`
2. Check it's in the right folder: `static/images/`
3. Hard refresh browser: Ctrl+F5
4. Check browser console for 404 errors (F12)
5. Restart Django server: Stop and `python manage.py runserver`

## Alternative: Use Copy Command
If you're comfortable with Windows command line:
```
copy "source\path\to\mvgr-image.jpg" "C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival\static\images\mvgr-campus.jpg"
```

## Testing
Once image is placed:
1. Visit http://localhost:8000/
2. You should see the MVGR building as background
3. The "Campus Carnival MVGR" text will overlay the building
4. Login/Register buttons will be visible on top

## Image Properties
- Recommended Size: 1600x900 pixels or larger
- Format: JPG/JPEG (best for web)
- File Size: Keep under 500KB for fast loading
- The image will be:
  - Fixed in place (parallax effect)
  - Covered with 35% dark overlay
  - Responsive on all devices

---

**Once you place the image file, your home page will look amazing! 🏛️**
