@echo off
echo ================================
echo Building Standalone Application
echo ================================
echo.

echo Installing required packages...
pip install -r requirements.txt

echo.
echo Building executable...
pyinstaller --onefile --windowed --name "MyAwesomeApp" --icon=NONE app.py

echo.
echo ================================
echo Build Complete!
echo ================================
echo Your executable is located in the 'dist' folder
echo File: dist\MyAwesomeApp.exe
echo.
pause
