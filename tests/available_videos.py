import sys
from pytube import YouTube
from pprint import pprint


yt = YouTube(sys.argv[1])
pprint(yt.get_videos())
