@echo off
REM Open the static images folder in Windows Explorer
REM This helps you quickly navigate to where to paste the image

echo.
echo ========================================
echo MVGR Campus Background Image Setup
echo ========================================
echo.
echo Opening the images folder...
echo Please paste your mvgr-campus.jpg image here
echo.
pause

start explorer "C:\Users\user\Desktop\ruhifinal\ruhifinall\sujuki\campuscarnival\static\images"

echo.
echo Folder opened! 
echo.
echo Next steps:
echo 1. Paste your image in this folder
echo 2. Rename it to: mvgr-campus.jpg
echo 3. Restart Django server (Ctrl+C then python manage.py runserver)
echo 4. Hard refresh browser: Ctrl+F5
echo 5. Visit http://localhost:8000/
echo.
pause
