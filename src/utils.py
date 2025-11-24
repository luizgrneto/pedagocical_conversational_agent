import os

def list_files_per_subject(root_directory: str):
    all_files = []
    for dir in os.listdir(root_directory):
        for dirpath, dirnames, filenames in os.walk(os.path.join(root_directory, dir)):
            for filename in filenames:
                all_files.append({'dirname': dir, 'file_path': os.path.join(dirpath, filename)})
    return all_files