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

def fetch_first_result(html_content):
    if not html_content:
        return html_content
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)
    if search_results and search_results[0]:
        logging.info("Found a result : " + search_results[0])
        return search_results[0]
    else:
        logging.warning("No result found")
        return None

# take highest mp4 resolution or else the last video
def download_video(url):
    yt = YouTube(url)
    if len(yt.filter('mp4')) > 0:
        video = yt.get('mp4', yt.filter('mp4')[-1].resolution)
    else:
        video = yt.getVideos()[-1]
    video.download(config.tmp_folder)
    return video

def download_first_result(search_query):
    if not search_query:
        return search_query
    req = urllib2.Request(format_youtube_query(search_query))
    response = urllib2.urlopen(req)
    fetched_result = fetch_first_result(response.read())
    if not fetched_result:
        return None
    url = "http://www.youtube.com/watch?v=" + fetched_result
    video = download_video(url)
    video_full_path = config.tmp_folder + video.filename + '.' + video.extension
    logging.info(video_full_path)
    return video_full_path
