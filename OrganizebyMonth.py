import os
import shutil
import hashlib
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def get_file_hash(file_path, buffer_size=65536):
    """Generates a hash for a file to detect duplicates."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(buffer_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_creation_month(file_path):
    """Gets the creation month and year of a file."""
    creation_time = os.path.getctime(file_path)
    creation_date = datetime.fromtimestamp(creation_time)
    return creation_date.strftime("%Y_%B")  # Format as "Year_Month" (e.g., "2023_January")

def organize_file(file_path, directory, file_hashes):
    """Organizes a single file by type and creation month, and removes duplicates."""
    filename = os.path.basename(file_path)
    if os.path.isfile(file_path):
        # Get file extension and create type folder
        file_ext = os.path.splitext(filename)[1][1:].lower()  # Remove the dot and get the extension
        type_folder = os.path.join(directory, file_ext + "_files")
        os.makedirs(type_folder, exist_ok=True)

        # Get creation month and create a month-based subfolder
        month_folder = get_creation_month(file_path)
        target_folder = os.path.join(type_folder, month_folder)
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

def organize_files_by_type_and_month(directory):
    """Organizes all files in the directory by type and creation month."""
    file_hashes = {}  # Dictionary to store file hashes for duplicate detection

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        organize_file(file_path, directory, file_hashes)

class FileOrganizerHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory
        self.file_hashes = {}  # Dictionary to store hashes for ongoing duplicate checks

    def on_modified(self, event):
        """Triggered when a file is modified or added."""
        if not event.is_directory:
            organize_file(event.src_path, self.directory, self.file_hashes)

if __name__ == "__main__":
    folder_to_track = r"C:\Users\pc\Documents\coding with ATOM"  # Replace with your directory path
    print("Organizing files by type and creation month...")

    # Organize existing files immediately
    organize_files_by_type_and_month(folder_to_track)
    print("Initial organization complete.")

    # Start monitoring for new files
    event_handler = FileOrganizerHandler(folder_to_track)
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=False)
    observer.start()

    try:
        print("Monitoring folder for new files...")
        while True:
            pass  # Keep the script running to monitor changes
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped monitoring.")
    observer.join()
