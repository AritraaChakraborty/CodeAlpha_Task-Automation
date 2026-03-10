import os
import shutil

def organize_photos():
    source_dir = "./my_files"  # Change this to your source folder path
    target_dir = "./organized_jpgs"

    # Create target folder if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    files_moved = 0
    # Check if source exists
    if os.path.exists(source_dir):
        for filename in os.listdir(source_dir):
            if filename.lower().endswith(".jpg"):
                source_path = os.path.join(source_dir, filename)
                shutil.move(source_path, target_dir)
                print(f"Moved: {filename}")
                files_moved += 1
        
        print(f"Done! Successfully moved {files_moved} files.")
    else:
        print("Source directory not found. Please check the path.")

# organize_photos() # Uncomment to run

