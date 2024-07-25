import os
import shutil

def add_files_to_directory(source_files, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for file_path in source_files:
        if os.path.isfile(file_path):
            try:
                shutil.copy(file_path, target_directory)
                print(f"Copied {file_path} to {target_directory}")
            except Exception as e:
                print(f"Failed to copy {file_path}: {e}")
        else:
            print(f"{file_path} is not a valid file")

if __name__ == "__main__":
    files = input("Enter the file paths to add (comma-separated): ").split(',')
    directory = input("Enter the target directory path: ")
    add_files_to_directory(files, directory)
