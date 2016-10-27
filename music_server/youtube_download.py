import logging

from pytube import YouTube

class YoutubeDownload:

    def __init__(self, video_url):
        self._video_url = video_url
        self._youtube_obj = YouTube(self._video_url)
        self._video = select_video(self._youtube_obj)

    # returns full path filename of the downloaded video
    def download(self, dest_folder):
        self._video.download(dest_folder)
        video_full_path = dest_folder + self._video.filename + '.' + self._video.extension
        logging.info(video_full_path)
        return video_full_path

# take highest mp4 resolution or else the last video in the list
def select_video(youtube_obj):
    if len(youtube_obj.filter('mp4')) > 0:
        video = youtube_obj.get('mp4', youtube_obj.filter('mp4')[-1].resolution)
    else:
        video = youtube_obj.getVideos()[-1]
    return video

#     def download_first_result(search_query):
#         if not search_query:
#             return search_query
#         req = urllib2.Request(format_youtube_query(search_query))
#         response = urllib2.urlopen(req)
#         fetched_result = fetch_results(response.read(), 1)
#         if not fetched_result:
#             return None
#         if not fetched_result[0]:
#             return None
#         url = "http://www.youtube.com/watch?v=" + fetched_result[0]
#         yt = YouTube(url)
#         video = select_video(yt)
#         video.download(config.tmp_folder)
#         video_full_path = config.tmp_folder + video.filename + '.' + video.extension
#         logging.info(video_full_path)
#         return video_full_path