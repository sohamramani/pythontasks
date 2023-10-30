import argparse
from a import *
from b import *
from c import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="Run the code")
    parser.add_argument("--file_manager", action="store_true", help="Run the code for file_manager work")
    parser.add_argument("--list", action="store_true", help="List files or folders in a directory.")
    parser.add_argument("--file", action="store_true", help="List files (only valid with --list).")
    parser.add_argument("--folder", action="store_true", help="List folders (only valid with --list).")
    parser.add_argument("--move", help="Move a file or folder to a destination.")
    parser.add_argument("--copy", help="Copy a file or folder to a destination.")
    parser.add_argument("--delete", help="Delete a file or folder.")
    parser.add_argument("--destination", help="Destination path for move or copy operations.")
    parser.add_argument("--sort", action="store_true", help="Enable sorting")
    parser.add_argument("--files", action="store_true", help="Sort files")
    parser.add_argument("--folders", action="store_true", help="Sort folders")
    parser.add_argument("--input_folder", help="Input folder for sorting")
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    compress_parser = subparsers.add_parser("compress", help="Compress a folder")
    compress_parser.add_argument("--sorter", action="store_true", help="Compress the sorter folder")
    compress_parser.add_argument("source_folder", help="Source folder to compress")
    compress_parser.add_argument("output_filename", help="Output filename for the compressed file")
    decompress_parser = subparsers.add_parser("decompress", help="Decompress a folder")
    decompress_parser.add_argument("zip_file", help="ZIP file to decompress")
    decompress_parser.add_argument("output_folder", help="Output folder for decompressed files")
    args = parser.parse_args()

    if args.run:
        if args.file_manager:
            if args.list:
                if args.file and args.folder:
                    print("Both --file and --folder cannot be specified together.")
                elif args.file:
                    list_files_or_folders(".", list_files=True)
                elif args.folder:
                    list_files_or_folders(".", list_files=False)
                else:
                    list_files_or_folders(".")
            elif args.move:
                if args.file:
                    move_file_or_folder(args.move, args.destination)
                elif args.folder:
                    move_file_or_folder(args.move, args.destination)
                else:
                    print("Please specify --file or --folder for move operation.")
            elif args.copy:
                if args.file:
                    copy_file_or_folder(args.copy, args.destination)
                elif args.folder:
                    copy_file_or_folder(args.copy, args.destination)
                else:
                    print("Please specify --file or --folder for copy operation.")
            elif args.delete:
                delete_file(args.delete)
            else:
                print("Please enter valid action")

        if  args.sort:
            input_folder = args.input_folder

            if not os.path.exists(input_folder):
                print(f"Input folder '{input_folder}' does not exist.")
                return

            if args.files:
                output_folder = 'sorted_files'
                is_folder_sort = False
            elif args.folders:
                output_folder = 'sorted_folders'
                is_folder_sort = True
            else:
                print("Invalid sort type. Use --files or --folders.")
                return
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            sort_files(input_folder, output_folder, is_folder_sort)

        if args.command == "compress":
            source_folder = args.source_folder
            if args.sorter:
                source_folder = os.path.join(source_folder, "sorted_files")
            compress_folder(source_folder, args.output_filename)

        elif args.command == "decompress":
            decompress_folder(args.zip_file, args.output_folder)

    main()