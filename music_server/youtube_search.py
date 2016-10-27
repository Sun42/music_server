import re
import urllib
import urllib2

import logging
from pprint import pprint
from objbrowser import browse

from pytube import YouTube

class YoutubeSearch:

    def __init__(self, search_query):
        self._youtube_url = format_youtube_query(search_query)
        self._html_content = get_html(self._youtube_url)
        self.video_ids = fetch_results(self._html_content)

def get_html(youtube_formated_url):
    req = urllib2.Request(youtube_formated_url)
    return urllib2.urlopen(req).read()

def format_youtube_query(search_query):
    url = "http://youtube.com/results?"
    data = {}
    data['search_query'] = search_query
    url_values = urllib.urlencode(data)
    youtube_query = url + url_values
    logging.info("Youtube query : " + youtube_query)
    return youtube_query

# Parse a youtube html response page and return N video IDs
# limit the number of returned IDs
# Would be cleaner to use the Youtube api
def fetch_results(html_content):
    results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)
    unique_list = []
    for result in results:
        str = 'https://www.youtube.com/watch?v=' + result
        if str not in unique_list:
            unique_list.append(str)
    return unique_list