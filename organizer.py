import os
import shutil
import time
import threading
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import getpass

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Organizer")
        self.root.geometry("400x600")

        # Extension groups
        self.grouped_extensions = {
            "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
            "Documents": ['.docx', '.doc', '.pdf', '.xlsx', '.txt'],
            "Media": ['.mp3', '.mp4'],
            "Archives": ['.zip']
        }

        self.folder_entries = {}
        self.target_dirs = {}
        self.running = False

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Drive Letter (for destination folders)").pack(pady=5)
        self.drive_entry = ttk.Entry(self.root)
        self.drive_entry.pack()

        ttk.Label(self.root, text="(Source folder is fixed: C:/Users/<You>/Downloads)").pack(pady=5)

        # Create one entry per group
        for group in self.grouped_extensions:
            ttk.Label(self.root, text=f"Target Folder for {group} files").pack(pady=2)
            entry = ttk.Entry(self.root)
            entry.pack()
            self.folder_entries[group] = entry

        self.start_button = ttk.Button(self.root, text="Start Organizer", command=self.start_organizer)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(self.root, text="Stop Organizer", command=self.stop_organizer, state='disabled')
        self.stop_button.pack(pady=5)

        self.status_label = ttk.Label(self.root, text="")
        self.status_label.pack(pady=10)

    def start_organizer(self):
        drive = self.drive_entry.get().upper()
        if not drive:
            messagebox.showerror("Missing Info", "Please provide a drive letter for targets.")
            return

        username = getpass.getuser()
        self.source_dir = f"C:/Users/{username}/Downloads"
        self.target_dirs = {}

        # Create target dirs and map extensions
        for group, entry in self.folder_entries.items():
            folder_name = entry.get()
            if not folder_name:
                continue
            path = os.path.join(f"{drive}:/", folder_name)
            os.makedirs(path, exist_ok=True)
            for ext in self.grouped_extensions[group]:
                self.target_dirs[ext] = path

        self.running = True
        self.status_label.config(text="Organizer is running...")
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        threading.Thread(target=self.organize_files, daemon=True).start()

    def stop_organizer(self):
        self.running = False
        self.status_label.config(text="Organizer stopped.")
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

    def organize_files(self):
        while self.running:
            try:
                file_names = os.listdir(self.source_dir)
                for file_name in file_names:
                    file_path = os.path.join(self.source_dir, file_name)
                    for ext, target_dir in self.target_dirs.items():
                        if file_name.lower().endswith(ext):
                            try:
                                shutil.move(file_path, target_dir)
                                self.log(f"Moved: {file_name}")
                            except Exception as e:
                                self.log(f"Error: {file_name} - {e}")
                            break
            except Exception as e:
                self.log(f"Directory error: {e}")
            time.sleep(5)

    def log(self, message):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
