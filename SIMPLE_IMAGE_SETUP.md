# 🏛️ SIMPLE IMAGE SETUP - 3 EASY STEPS

## Your Task
Add the MVGR college building image as the home page background.

---

## 3 SIMPLE STEPS

### ✅ Step 1: Find Your Image
You have the MVGR campus building image. You need to:
- Find it on your computer
- Remember where it is
- Make sure it's in JPG format

### ✅ Step 2: Save It to This Folder
```
C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival\static\images\
```

**Name it exactly**: `mvgr-campus.jpg`

**How to do it**:
1. Right-click the image
2. Select "Save image as" OR "Copy"
3. Navigate to the folder above
4. Save/Paste it there
5. Rename to `mvgr-campus.jpg`

### ✅ Step 3: Refresh the Website
1. Go to: `http://localhost:8000/`
2. Press: `Ctrl+F5` (hard refresh)
3. Done! You should see the image as background

---

## The Quickest Way

### Using Windows Explorer
1. Press: `Win + E` (open File Explorer)
2. Paste this in address bar:
   ```
   C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival\static\images\
   ```
3. Drag and drop your image into this folder
4. Rename it to: `mvgr-campus.jpg`
5. Refresh browser at `http://localhost:8000/`

---

## Visual Guide

### Where to Put Image
```
My Computer
  ↓
Users
  ↓
user
  ↓
Desktop
  ↓
ruhifinal
  ↓
ruhifinall
  ↓
sujuki
  ↓
campuscarnival
  ↓
static
  ↓
images  ← PUT IMAGE HERE
```

### File Name
```
WRONG: image.jpg, mvgr.jpg, campus.jpg
RIGHT: mvgr-campus.jpg
```

---

## Done?

After you add the image and refresh:
- ✅ MVGR building shows as background
- ✅ "Campus Carnival MVGR" text is visible
- ✅ Login/Register buttons work
- ✅ Everything looks professional!

---

## If It Doesn't Work

**Most common issues**:
1. Filename not exactly `mvgr-campus.jpg`
   - Fix: Rename the file
   
2. File in wrong folder
   - Fix: Move to `static/images/`
   
3. Browser cached old page
   - Fix: Press `Ctrl+F5` to hard refresh
   
4. Django not running
   - Fix: Start with `python manage.py runserver`

---

## Need Help?

Run this to check everything:
```
python setup_image.py
```

It will tell you if image is in the right place!

---

**That's it! Three simple steps and your home page will have the beautiful MVGR campus background! 🏛️**
