#!flask/bin/python

import moviepy.editor as mp

def video_to_mp3(video_filename):
    clip = mp.VideoFileClip(video_filename)
    audio_filename = video_filename + ".mp3"
    clip.audio.write_audiofile(audio_filename)
    return audio_filename
