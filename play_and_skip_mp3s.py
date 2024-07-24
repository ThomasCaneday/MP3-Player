import os
import pygame

class MusicPlayer:
    def __init__(self, directory):
        self.directory = directory
        self.mp3_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
        self.mp3_files.sort()
        self.current_index = 0
        self.is_playing = False

        pygame.mixer.init()

    def play_next(self):
        if self.current_index < len(self.mp3_files):
            mp3_path = os.path.join(self.directory, self.mp3_files[self.current_index])
            print(f"Now playing: {self.mp3_files[self.current_index]}")
            pygame.mixer.music.load(mp3_path)
            pygame.mixer.music.play()
            self.is_playing = True
        else:
            print("No more songs in the playlist.")
            self.is_playing = False

    def skip_song(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            self.current_index += 1
            self.play_next()

    def play(self):
        if not self.is_playing:
            self.play_next()

    def is_music_playing(self):
        return pygame.mixer.music.get_busy()

# Example usage
if __name__ == "__main__":
    import argparse
    import time

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Play and skip MP3 files in a directory")
    parser.add_argument("directory", help="Path to the directory containing MP3 files")

    args = parser.parse_args()

    player = MusicPlayer(args.directory)
    player.play()

    # Simulate playing and skipping songs
    while player.is_music_playing():
        print("Press 's' to skip the current song")
        if input().strip().lower() == 's':
            player.skip_song()

        # Add a small delay to avoid busy-waiting
        time.sleep(0.1)

    print("Finished playing all MP3 files.")
