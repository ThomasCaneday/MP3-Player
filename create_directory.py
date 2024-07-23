import os

def create_directory(directory_path):
    try:
        # Create target directory
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory '{directory_path}' created successfully")
    except Exception as e:
        print(f"An error occurred while creating the directory: {e}")

# Example usage
if __name__ == "__main__":
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Create a directory")
    parser.add_argument("directory", help="Path of the directory to be created")

    args = parser.parse_args()

    create_directory(args.directory)
