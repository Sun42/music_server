import moviepy.editor as mp
import string

def video_to_audio(video_filename):
    clip = mp.VideoFileClip(video_filename)
    audio_filename = remove_extension(video_filename) + '.mp3'
    clip.audio.write_audiofile(audio_filename)
    return audio_filename


def remove_extension(video_filename):
    if not video_filename:
        return video_filename
    tab = string.rsplit(video_filename, '.', 1)
    if len(tab) > 1:
        trimmed_filename = string.rstrip(video_filename, '.' + tab[1])
        return trimmed_filename
    else:
        return video_filename
