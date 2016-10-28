import logging

from pytube import YouTube

class YoutubeDownload:

    def __init__(self, video_url):
        self._video_url = video_url
        self._youtube_obj = YouTube(self._video_url)
        self._video = select_video(self._youtube_obj)

    # returns full path filename of the downloaded video
    def download(self, dest_folder):
        video_full_path = dest_folder + self._video.filename + '.' + self._video.extension
        self._video.download(dest_folder)
        logging.info(video_full_path)
        return video_full_path

# take highest mp4 resolution or else the last video in the list
def select_video(youtube_obj):
    if len(youtube_obj.filter('mp4')) > 0:
        video = youtube_obj.get('mp4', youtube_obj.filter('mp4')[-1].resolution)
    else:
        video = youtube_obj.getVideos()[-1]
    return video
