import os
import shutil
from datetime import datetime

def create_folder(base_folder, folder_name):
    folder_path = os.path.join(base_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def move_file_or_folder(src, dest):
    try:
        shutil.move(src, dest)
        print(f"Moved: {src} -> {dest}")
    except Exception as e:
        print(f"Error moving {src} to {dest}: {str(e)}")

def sort_files(input_folder, output_folder, is_folder_sort):
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        if os.path.isfile(item_path):
            creation_date = datetime.fromtimestamp(os.path.getctime(item_path))
            year = creation_date.year
            month = creation_date.strftime('%B')
            week = f'week_{creation_date.strftime("%U")}'
            year_folder = create_folder(output_folder, str(year))
            month_folder = create_folder(year_folder, month)
            week_folder = create_folder(month_folder, week)
            move_file_or_folder(item_path, os.path.join(week_folder, item))
        elif is_folder_sort and os.path.isdir(item_path) and item != output_folder:
            move_file_or_folder(item_path, output_folder)
    return output_folder