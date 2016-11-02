import os
import string
import re

separator = '-'

def clean_dir(path_to_dir):
    if not os.path.isdir(path_to_dir):
        os.mkdir(path_to_dir)
    file_list = os.listdir(path_to_dir)
    for file_name in file_list:
        os.remove(path_to_dir + "/" + file_name)

# extract filename with extension
def extract_filename(file_path):
    filename = os.path.basename(file_path)
    return filename

def remove_extension(video_filename):
    if not video_filename:
        return video_filename
    return os.path.splitext(video_filename)[0]
