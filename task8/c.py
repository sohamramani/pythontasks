import os
import zipfile

def compress_folder(source_folder, output_filename):
    try:
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_folder)
                    zipf.write(file_path, arcname=arcname)
        print(f"Compressed {source_folder} to {output_filename}")
    except Exception as e:
        print(f"Error compressing {source_folder}: {str(e)}")

def decompress_folder(zip_file, output_folder):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall(output_folder)
        print(f"Decompressed {zip_file} to {output_folder}")
    except Exception as e:
        print(f"Error decompressing {zip_file}: {str(e)}")