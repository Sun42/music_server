import moviepy.editor as mp
from util import remove_extension

def video_to_audio(video_filename):
    clip = mp.VideoFileClip(video_filename)
    audio_filename = remove_extension(video_filename) + '.mp3'
    clip.audio.write_audiofile(audio_filename)
    return audio_filename
