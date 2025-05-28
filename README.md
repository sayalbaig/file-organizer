# 🗂️ Smart File Organizer

A simple and customizable Python-based GUI application that automatically organizes files from your **Downloads folder** into categorized directories (Images, Documents, Media, Archives) based on file extensions.

## ✨ Features

- ✅ Automatically moves files from `C:/Users/<you>/Downloads`
- ✅ Supports all common image, document, media, and archive formats
- ✅ Easy-to-use GUI with no coding required
- ✅ Lets you choose the destination drive and folder names
- ✅ Start and stop the organizer anytime
- ✅ Bundled into a standalone `.exe` (no need for Python)

---

## 📁 File Types Supported

| Category   | Extensions                                            |
|------------|--------------------------------------------------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`, `.svg` |
| Documents  | `.doc`, `.docx`, `.pdf`, `.xlsx`, `.txt`              |
| Media      | `.mp3`, `.mp4`                                        |
| Archives   | `.zip`                                                |

---

## 🖥️ How to Use

### 📦 Option 1: Download `.exe`

1. Run the `.exe` file (provided in the [Releases](#) tab).
2. Enter:
   - The drive letter (e.g., `D`)
   - Folder names where each category should be moved
3. Click **Start Organizer** to begin auto-sorting.
4. Click **Stop Organizer** to pause at any time.

> 💡 The source folder is always `C:/Users/<YourName>/Downloads`

---

### 🛠️ Option 2: Run From Python Script

1. Install dependencies (if not already):
   ```bash
   pip install tk

2. Run the script:
  python organizer.py

