import logging

import moviepy.editor as mp

import util

def video_to_audio(video_full_path, dest_folder):
    logging.debug("Arg1" + video_full_path)
    logging.debug("Arg2" + dest_folder)
    clip = mp.VideoFileClip(video_full_path)
    audio_full_path = dest_folder + util.remove_extension(util.extract_filename(video_full_path)) + '.mp3'
    clip.audio.write_audiofile(audio_full_path)
    return audio_full_path
