# My Awesome App

A simple, modern Windows desktop application with a graphical interface.

## Features

- ✨ Clean and modern GUI
- 👤 User greeting functionality
- 📦 Packageable as standalone .exe
- 🚀 No installation required (once built)

## How to Run (Development)

1. Make sure Python is installed on your system
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python app.py
   ```

## How to Build a Downloadable .exe

1. Double-click `build_app.bat` (or run it in PowerShell)
2. Wait for the build process to complete
3. Find your executable in the `dist` folder: `dist\MyAwesomeApp.exe`
4. You can now distribute this .exe file to anyone!

## Building Manually

If you prefer to build manually:

```powershell
pip install pyinstaller
pyinstaller --onefile --windowed --name "MyAwesomeApp" app.py
```

## Distribution

Once built, you can:
- Share the .exe file directly with others
- Upload it to cloud storage (Google Drive, Dropbox, etc.)
- Create a setup installer using tools like Inno Setup
- Distribute it however you like!

## Requirements

- Python 3.7 or higher (for development/building)
- No requirements for running the .exe (fully standalone)

## Customization

Feel free to modify `app.py` to add your own features:
- Change the title and branding
- Add new buttons and functionality
- Customize colors and styling
- Add more complex features

Enjoy your app! 🎉
