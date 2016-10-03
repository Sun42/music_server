#!flask/bin/python

import urllib
import urllib2
import re
from pprint import pprint
from pytube import YouTube

def download_first_result(search_query):
    url = "http://youtube.com/results?"
    data = {}
    data['search_query'] = search_query
    url_values = urllib.urlencode(data)
    print("Url request : " + url + url_values)
    req = urllib2.Request(url + url_values)
    response = urllib2.urlopen(req)
    html_content = response.read()
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)
    pprint(search_results)
    # print("http://www.youtube.com/watch?v=" + search_results[0])

    yt = YouTube("http://www.youtube.com/watch?v=" + search_results[0])

    # pprint(yt.get_videos())
    # print(yt.filter('mp4')[-1])
    video = yt.get('mp4')
    video.download('./tmp/')
    # print(dir(video))
    return './tmp/' + video.filename + '.' + video.extension
