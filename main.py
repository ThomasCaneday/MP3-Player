import os
from create_directory import create_directory
from add_files_to_directory import add_files_to_directory
from play_and_skip_mp3s import MusicPlayer
from convert_mp4_to_mp3 import convert_mp4_to_mp3

def display_menu():
    print("\nSelect a program to run:")
    print("1. Create a Directory")
    print("2. Add Files to a Directory")
    print("3. Play MP3s in a Directory")
    print("4. Convert MP4 to MP3")
    print("5. Exit")

def run_program(choice):
    if choice == '1':
        directory = input("Enter the directory path to create: ")
        create_directory(directory)
    elif choice == '2':
        files = input("Enter the file paths to add (comma-separated): ").split(',')
        directory = input("Enter the target directory path: ")
        add_files_to_directory(files, directory)
    elif choice == '3':
        directory = input("Enter the directory path containing MP3 files: ")
        player = MusicPlayer(directory)
        player.play()
        while player.is_music_playing():
            print("Press 's' to skip the current song")
            if input().strip().lower() == 's':
                player.skip_song()
    elif choice == '4':
        input_path = input("Enter the MP4 file or directory path containing MP4 files: ")
        output_path = input("Enter the directory path to save MP3 files: ")
        if os.path.isfile(input_path):
            mp3_file = convert_mp4_to_mp3(input_path, output_path)
            print(f"MP3 file saved as: {mp3_file}")
        elif os.path.isdir(input_path):
            for file_name in os.listdir(input_path):
                if file_name.endswith(".mp4"):
                    mp4_file = os.path.join(input_path, file_name)
                    mp3_file = convert_mp4_to_mp3(mp4_file, output_path)
                    print(f"MP3 file saved as: {mp3_file}")
        else:
            print("Invalid input path. Please provide a valid MP4 file or directory containing MP4 files.")
    elif choice == '5':
        print("Exiting the menu.")
        return
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '5':
            break
        run_program(choice)
