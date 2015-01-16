import os


def check_files(root, file_name_list):
    for file_name in file_name_list:
        file_path = os.path.join(root, file_name)
        if not os.path.isfile(file_path):
            raise ValueError("File not exist: " + file_path)

def ensure_dir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
