import os
import shutil

# path of the folder which needs to be organised
path = "C:/Users/Abhisekh/Downloads/test_organise"

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".tiff", ".heic", ".webp"],
    "videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "software": [".exe", ".msi", ".dmg", ".pkg"],
    "documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".bz2"],
    
}


# Function to create directories if they don't exist

def create_directories():
    for directory in file_types.keys():
        dir_path = os.path.join(path, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

# Function to move files to their respective directories
def move_files():
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Move files based on their extensions
        for directory, extensions in file_types.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):
                dest_path = os.path.join(path, directory, file_name)
                shutil.move(file_path, dest_path)
                print(f"Moved: {file_name} -> {directory}")
                break

# Main function
def main():
    create_directories()
    move_files()

if __name__ == "__main__":
    main()
    