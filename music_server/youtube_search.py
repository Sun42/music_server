import re
import urllib
import urllib2

import logging
from pprint import pprint
from objbrowser import browse

from pytube import YouTube

class YoutubeSearch:

    def __init__(self, search_query):
        self._query_url = format_query(search_query)
        self._html_content = get_html(self._query_url)
        self.video_ids = fetch_results(self._html_content)
def get_html(url):
    req = urllib2.Request(url)
    return urllib2.urlopen(req).read()

def format_query(search_query):
    #@todo generic class .query
    url = "http://youtube.com/results?"
    data = {}
    data['search_query'] = search_query
    url_values = urllib.urlencode(data)
    query = url + url_values
    logging.info("Query : " + query)
    return query

# Parse a youtube html response page and return N video IDs
# limit the number of returned IDs
# Would be cleaner to use the Youtube api
def fetch_results(html_content):
    results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)
    unique_list = []
    for result in results:
        if result not in unique_list:
            unique_list.append(result)
    return unique_list