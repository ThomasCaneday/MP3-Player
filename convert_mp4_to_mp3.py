from pydub import AudioSegment
import os

def convert_mp4_to_mp3(mp4_file, output_path):
    # Extract filename without extension
    base = os.path.splitext(os.path.basename(mp4_file))[0]
    mp3_file = os.path.join(output_path, base + '.mp3')

    # Convert mp4 to mp3
    audio = AudioSegment.from_file(mp4_file, format="mp4")
    audio.export(mp3_file, format="mp3")

    return mp3_file

# Example usage
if __name__ == "__main__":
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert MP4 videos to MP3 audios")
    parser.add_argument("input_path", help="Path to the MP4 file or directory containing MP4 files")
    parser.add_argument("output_path", help="Directory to save the MP3 files")

    args = parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path

    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if os.path.isfile(input_path):
        # Convert single file
        mp3_file = convert_mp4_to_mp3(input_path, output_path)
        print(f"MP3 file saved as: {mp3_file}")
    elif os.path.isdir(input_path):
        # Convert all MP4 files in the directory
        for file_name in os.listdir(input_path):
            if file_name.endswith(".mp4"):
                mp4_file = os.path.join(input_path, file_name)
                mp3_file = convert_mp4_to_mp3(mp4_file, output_path)
                print(f"MP3 file saved as: {mp3_file}")
    else:
        print("Invalid input path. Please provide a valid MP4 file or directory containing MP4 files.")
