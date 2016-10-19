import urllib
import urllib2
import re
import config
import logging
from pprint import pprint
from pytube import YouTube

def format_youtube_query(search_query):
    url = "http://youtube.com/results?"
    data = {}
    data['search_query'] = search_query
    url_values = urllib.urlencode(data)
    youtube_query = url + url_values
    logging.info("Youtube query : " + youtube_query)
    return youtube_query

def fetch_results(html_content, limit = 0):
    if not html_content:
        return html_content
    results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)
    if not results:
        logging.warning("No result found")
        return None
    if not limit:
        return results
    return results[:limit]

# take highest mp4 resolution or else the last video in the list
def select_video(youtube_obj):
    if len(youtube_obj.filter('mp4')) > 0:
        video = youtube_obj.get('mp4', youtube_obj.filter('mp4')[-1].resolution)
    else:
        video = youtube_obj.getVideos()[-1]
    return video

def download_first_result(search_query):
    if not search_query:
        return search_query
    req = urllib2.Request(format_youtube_query(search_query))
    response = urllib2.urlopen(req)
    fetched_result = fetch_results(response.read(), 1)
    if not fetched_result:
        return None
    if not fetched_result[0]:
        return None
    url = "http://www.youtube.com/watch?v=" + fetched_result[0]
    yt = YouTube(url)
    video = select_video(yt)
    video.download(config.tmp_folder)
    video_full_path = config.tmp_folder + video.filename + '.' + video.extension
    logging.info(video_full_path)
    return video_full_path
