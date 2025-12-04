# Distribution & Update Guide

## 📥 How to Get Your App

### Building the App:
1. Double-click `build_app.bat` in this folder
2. Wait for the build to complete
3. Find `MyAwesomeApp.exe` in the `dist` folder
4. That's your distributable app!

### Distributing to Users:
- **Email:** Attach the .exe file
- **Cloud Storage:** Upload to Google Drive, Dropbox, OneDrive and share the link
- **USB Drive:** Copy the .exe and hand it to people
- **Website:** Host it on your own site
- **GitHub:** Create a release and upload the .exe

## 🔄 Setting Up Auto-Updates (Optional)

Your app now has a "Check Updates" button! Here's how to make it work:

### Step 1: Host Your App
Upload `MyAwesomeApp.exe` somewhere accessible:
- GitHub Releases (recommended for free hosting)
- Your own website
- Dropbox/Google Drive (with public link)

### Step 2: Create version.json
Upload this file to the same place (or GitHub):
```json
{
  "version": "1.0.1",
  "download_url": "https://direct-link-to-your-app.exe",
  "changelog": "Bug fixes and new features"
}
```

### Step 3: Update the Code
In `app.py`, change this line:
```python
UPDATE_URL = "https://your-actual-url/version.json"
```

### Step 4: When You Release Updates
1. Build new version with `build_app.bat`
2. Upload the new .exe
3. Update `version.json` with new version number and download link
4. Users click "Check Updates" and get notified!

## 🚀 Quick GitHub Setup (Recommended)

1. Create a GitHub repository
2. Go to "Releases" → "Create a new release"
3. Upload your .exe file
4. Upload version.json to your repo
5. Use the raw GitHub URL in UPDATE_URL

Example URL:
```
https://raw.githubusercontent.com/yourusername/yourapp/main/version.json
```

## 💡 Alternative: Simple Manual Updates

If you don't want auto-update:
- Just rebuild the app when you make changes
- Share the new .exe with users
- They replace their old file with the new one

## 📝 Version Numbers

Update the VERSION in app.py when you make changes:
```python
VERSION = "1.0.0"  # Change to 1.0.1, 1.1.0, 2.0.0, etc.
```

Happy distributing! 🎉
