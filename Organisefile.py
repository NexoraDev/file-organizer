import os
import shutil
import hashlib
import time
from PIL import Image
from pdf2image import convert_from_path

def get_file_hash(file_path, buffer_size=65536):
    """Generates a hash for a file to detect duplicates."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(buffer_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def create_preview_image(file_path, target_folder):
    """Creates a preview image for the first document in the folder."""
    preview_path = os.path.join(target_folder, "preview.jpg")
    
    if file_path.lower().endswith('.pdf'):
        # Convert the first page of the PDF to an image
        images = convert_from_path(file_path, first_page=0, last_page=1)
        images[0].save(preview_path, 'JPEG')
    elif file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Resize and save a preview of the image file
        with Image.open(file_path) as img:
            img.thumbnail((200, 200))  # Resize for preview
            img.save(preview_path, 'JPEG')
    else:
        print(f"No preview created for file type: {file_path}")

def organize_files(directory):
    """Organizes files in the directory based on file types and detects duplicates."""
    file_hashes = {}  # Dictionary to store file hashes for duplicate detection

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Get file extension and create folder for it
            file_ext = os.path.splitext(filename)[1][1:].lower()  # Remove the dot and get the extension
            target_folder = os.path.join(directory, file_ext + "_files")
            os.makedirs(target_folder, exist_ok=True)

            # Check for duplicate files
            file_hash = get_file_hash(file_path)
            file_size = os.path.getsize(file_path)
            file_key = (file_ext, file_hash, file_size)

            if file_key in file_hashes:
                print(f"Duplicate found and removed: {filename}")
                os.remove(file_path)  # Remove duplicate file
            else:
                # Move file to the target folder and record hash
                shutil.move(file_path, os.path.join(target_folder, filename))
                file_hashes[file_key] = os.path.join(target_folder, filename)

                # Create a preview image if this is the first file in the folder
                if not os.path.exists(os.path.join(target_folder, "preview.jpg")):
                    create_preview_image(os.path.join(target_folder, filename), target_folder)

if __name__ == "__main__":
    folder_to_track = r"C:\Users\pc\Documents"  # Replace with your directory path

    print("Starting daily file organization...")

    while True:
        print("Organizing files...")
        organize_files(folder_to_track)
        print("Files organized. Next check in 24 hours.")

        # Wait for 24 hours (24 hours * 60 minutes * 60 seconds)
        time.sleep(24 * 60 * 60)
