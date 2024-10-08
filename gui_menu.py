import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, StringVar
import threading
from create_directory import create_directory
from add_files_to_directory import add_files_to_directory
from play_and_skip_mp3s import MusicPlayer
from convert_mp4_to_mp3 import convert_mp4_to_mp3
# PyTubeFix (8-8-24)
from pytubefix import YouTube
from pytubefix.cli import on_progress

# from pytube import cipher
# import re

# from pytube.innertube import _default_clients
# from pytube import cipher
# import re

# _default_clients["ANDROID"]["context"]["client"]["clientVersion"] = "19.08.35"
# _default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
# _default_clients["ANDROID_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
# _default_clients["IOS_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
# _default_clients["IOS_MUSIC"]["context"]["client"]["clientVersion"] = "6.41"
# _default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]



# def get_throttling_function_name(js: str) -> str:
#     """Extract the name of the function that computes the throttling parameter.

#     :param str js:
#         The contents of the base.js asset file.
#     :rtype: str
#     :returns:
#         The name of the function used to compute the throttling parameter.
#     """
#     function_patterns = [
#         r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
#         r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
#         r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
#     ]
#     #logger.debug('Finding throttling function name')
#     for pattern in function_patterns:
#         regex = re.compile(pattern)
#         function_match = regex.search(js)
#         if function_match:
#             #logger.debug("finished regex search, matched: %s", pattern)
#             if len(function_match.groups()) == 1:
#                 return function_match.group(1)
#             idx = function_match.group(2)
#             if idx:
#                 idx = idx.strip("[]")
#                 array = re.search(
#                     r'var {nfunc}\s*=\s*(\[.+?\]);'.format(
#                         nfunc=re.escape(function_match.group(1))),
#                     js
#                 )
#                 if array:
#                     array = array.group(1).strip("[]").split(",")
#                     array = [x.strip() for x in array]
#                     return array[int(idx)]

#     raise re.RegexMatchError(
#         caller="get_throttling_function_name", pattern="multiple"
#     )

# cipher.get_throttling_function_name = get_throttling_function_name

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python MP3 Player Menu")
        self.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.create_directory_frame()
        self.add_files_frame()
        self.play_mp3s_frame()
        self.convert_mp4_frame()
        self.download_youtube_frame()
        
        tk.Button(self, text="Exit", command=self.quit).pack(pady=10)

    def create_directory_frame(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="Create Directory:").grid(row=0, column=0)
        self.create_dir_entry = tk.Entry(frame, width=50)
        self.create_dir_entry.grid(row=0, column=1)
        tk.Button(frame, text="Create", command=self.create_directory).grid(row=0, column=2)

    def create_directory(self):
        directory = self.create_dir_entry.get().strip()
        if directory:
            message = create_directory(directory)
            messagebox.showinfo("Create Directory", message)
        else:
            messagebox.showwarning("Input Error", "Please enter a directory path.")

    def add_files_frame(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="Add Files (comma-separated):").grid(row=0, column=0)
        self.add_files_entry = tk.Entry(frame, width=50)
        self.add_files_entry.grid(row=0, column=1)

        tk.Label(frame, text="Target Directory:").grid(row=1, column=0)
        self.target_dir_entry = tk.Entry(frame, width=50)
        self.target_dir_entry.grid(row=1, column=1)

        tk.Button(frame, text="Add", command=self.add_files_to_directory).grid(row=2, column=1)

    def add_files_to_directory(self):
        files = self.add_files_entry.get().strip().split(',')
        target_directory = self.target_dir_entry.get().strip()
        if files and target_directory:
            message = add_files_to_directory(files, target_directory)
            messagebox.showinfo("Add Files to Directory", message)
        else:
            messagebox.showwarning("Input Error", "Please enter valid file paths and target directory.")

    def play_mp3s_frame(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="MP3 Directory:").grid(row=0, column=0)
        self.mp3_dir_entry = tk.Entry(frame, width=50)
        self.mp3_dir_entry.grid(row=0, column=1)
        tk.Button(frame, text="Play", command=self.play_mp3s).grid(row=0, column=2)

    def play_mp3s(self):
        directory = self.mp3_dir_entry.get().strip()
        if directory:
            player = MusicPlayer(directory)
            player_thread = threading.Thread(target=self.play_music, args=(player,))
            player_thread.start()
        else:
            messagebox.showwarning("Input Error", "Please enter a valid directory path.")

    def play_music(self, player):
        player.play()
        while player.is_music_playing():
            skip = messagebox.askyesno("Skip Song", "Do you want to skip the current song?")
            if skip:
                player.skip_song()

    def convert_mp4_frame(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="MP4 File Path:").grid(row=0, column=0)
        self.mp4_file_entry = tk.Entry(frame, width=50)
        self.mp4_file_entry.grid(row=0, column=1)

        tk.Label(frame, text="Output Directory:").grid(row=1, column=0)
        self.output_dir_entry = tk.Entry(frame, width=50)
        self.output_dir_entry.grid(row=1, column=1)

        tk.Button(frame, text="Convert", command=self.convert_mp4_to_mp3).grid(row=2, column=1)

    def convert_mp4_to_mp3(self):
        input_path = self.mp4_file_entry.get().strip()
        output_path = self.output_dir_entry.get().strip()
        if input_path and output_path:
            mp3_file = convert_mp4_to_mp3(input_path, output_path)
            messagebox.showinfo("Convert MP4 to MP3", f"MP3 file saved as: {mp3_file}")
        else:
            messagebox.showwarning("Input Error", "Please enter valid file paths.")

    def download_youtube_frame(self):
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Label(frame, text="YouTube URL:").grid(row=0, column=0)
        self.youtube_url_entry = tk.Entry(frame, width=50)
        self.youtube_url_entry.grid(row=0, column=1)
        tk.Button(frame, text="Download", command=self.download_youtube_video).grid(row=1, column=1)

    def download_youtube_video(self):
        url = self.youtube_url_entry.get().strip()
        if url:
            try:
                yt = YouTube(url, on_progress_callback = on_progress)
                video = yt.streams.first()
                video.download()
                messagebox.showinfo("Download YouTube Video", "Video downloaded successfully!")
            except Exception as e:
                messagebox.showerror("Download Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid YouTube URL.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
