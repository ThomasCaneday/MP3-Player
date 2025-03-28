import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yt_dlp

def progress_hook(d):
    """Updates the progress bar based on yt-dlp's progress reports."""
    if d['status'] == 'downloading':
        # Try to get the total bytes; it may be under a different key.
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        if total_bytes:
            downloaded = d.get('downloaded_bytes', 0)
            percent = (downloaded / total_bytes) * 100
            progress_var.set(percent)
            progress_label.config(text=f"Download Progress: {int(percent)}%")
            root.update_idletasks()
    elif d['status'] == 'finished':
        progress_label.config(text="Download complete!")

def download_video():
    """Downloads the YouTube video using yt-dlp."""
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    # Let the user choose a folder for saving the file.
    folder = filedialog.askdirectory(title="Select Download Folder")
    if not folder:
        return

    # Options for yt-dlp:
    ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Force mp4 format if available
    'merge_output_format': 'mp4',  # Merge video and audio into an mp4 container if necessary
    'outtmpl': f'{folder}/%(title)s.%(ext)s',
    'progress_hooks': [progress_hook],
    'noplaylist': True,
}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error during download:\n{e}")

# Set up the main application window.
root = tk.Tk()
root.title("YouTube Video Downloader (yt-dlp)")
root.geometry("600x300")

# URL entry and label.
tk.Label(root, text="Enter YouTube Video URL:", font=("Helvetica", 14)).pack(pady=10)
url_entry = tk.Entry(root, width=80, font=("Helvetica", 12))
url_entry.pack(pady=5)

# Download button.
download_btn = tk.Button(root, text="Download Video", font=("Helvetica", 12), command=download_video)
download_btn.pack(pady=10)

# Progress bar and label.
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, orient="horizontal", length=500, mode="determinate")
progress_bar.pack(pady=10)
progress_label = tk.Label(root, text="Download Progress: 0%", font=("Helvetica", 12))
progress_label.pack(pady=5)

root.mainloop()
