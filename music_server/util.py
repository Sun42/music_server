import os

def clean_dir(path_to_dir):
    if not os.path.isdir(path_to_dir):
        os.mkdir(path_to_dir)
    file_list = os.listdir(path_to_dir)
    for file_name in file_list:
        os.remove(path_to_dir + "/" + file_name)