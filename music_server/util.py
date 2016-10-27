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

# deprecated
def make_audio_name(artist_name, title):
    new_audio_name = normalize(artist_name) + separator + normalize(title) + '.mp3'
    return new_audio_name

#  deprecated
def normalize(name):
    normalized_str = string.lower(name)
    normalized_str = string.replace(normalized_str, '-', ' ')
    normalized_str = string.strip(normalized_str)
    normalized_str = string.replace(normalized_str, ' ', '_')
    normalized_str = re.sub('\s+', '_', normalized_str)
    return normalized_str
# deprecated
def find_in_filesystem(directory, song):
    return os.path.exists(directory + song)