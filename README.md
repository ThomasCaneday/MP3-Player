# MP3 Player

This is a Python-based MP3 Player Program with a graphical user interface (GUI) that allows users to create directories, add files to directories, play MP3 files from a specified directory, convert MP4 files to MP3, and download YouTube videos. The GUI is built using `tkinter`.

## Features

1. **Create Directory**: Create a new directory by specifying the path.
2. **Add Files to Directory**: Add files to a specified directory.
3. **Play MP3s in a Directory**: Play MP3 files from a specified directory, with the ability to skip the current song.
4. **Convert MP4 to MP3**: Convert MP4 video files to MP3 audio files.
5. **YouTube Video Downloader**: Download YouTube videos directly from the GUI.

## Prerequisites

- Python 3.x
- `pydub` library
- `pygame` library
- `tkinter` library (usually included with Python)
- `pytube` library

You can install the required libraries using `pip`:
```bash
pip install pydub pygame tk pytube
```
Additionally, you need to have `ffmpeg` installed for audio conversion.

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/thomascaneday/mp3-player.git
cd mp3-player
```
2. **Install the required Python packages**:
```bash
pip install -r requirements.txt
```
3. **Ensure ffmpeg is installed and accessible from your system's PATH.**

## Usage

Run the gui_menu.py script to start the program:
```bash
python gui_menu.py
```
