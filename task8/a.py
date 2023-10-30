import os
import shutil

def list_files_or_folders(directory, list_files=True):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    if list_files:
        items = [item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))]
        print("Files in directory:")
    else:
        items = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))]
        print("Folders in directory:")

    for item in items:
        print(item)
        
    return directory

def move_file_or_folder(src, destination):
    try:
        shutil.move(src, destination)
        print(f"Moved '{src}' to '{destination}'.")
    except Exception as e:
        print(f"Error moving '{src}' to '{destination}': {str(e)}")

def copy_file_or_folder(src, destination):
    try:
        shutil.copy(src, destination)
        print(f"Copied '{src}' to '{destination}'.")
    except Exception as e:
        print(f"Error copying '{src}' to '{destination}': {str(e)}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"Deleted '{file_name}'.")
    except Exception as e:
        print(f"Error deleting '{file_name}': {str(e)}")