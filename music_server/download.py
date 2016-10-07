import urllib
import urllib2
import re
import config
from pprint import pprint
from pytube import YouTube

def format_youtube_query(search_query):
    url = "http://youtube.com/results?"
    data = {}
    data['search_query'] = search_query
    url_values = urllib.urlencode(data)
    youtube_query = url + url_values
    print("Youtube query : " + youtube_query)
    return youtube_query

def fetch_first_result(html_content):
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)
    return search_results[0]

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
    req = urllib2.Request(format_youtube_query(search_query))
    response = urllib2.urlopen(req)
    url = "http://www.youtube.com/watch?v=" + fetch_first_result(response.read())
    video = download_video(url)
    return config.tmp_folder + video.filename + '.' + video.extension
