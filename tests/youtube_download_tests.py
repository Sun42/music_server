import os
import mock
import unittest

from objbrowser import browse
from pytube import YouTube
from pytube import api

from .context import music_server
from music_server import youtube_download
from music_server import util
from music_server import config

class YoutubeDownloadTestCase(unittest.TestCase):

    def tearDown(self):
        pass
        music_server.util.clean_dir(config.tmp_folder)

    # when multiple video format, prefer the mp4
    # <Video: MPEG-4 Visual (.3gp) - 144p - Simple>,
    # <Video: MPEG-4 Visual (.3gp) - 240p - Simple>,
    # <Video: H.264 (.mp4) - 360p - Baseline>,
    # <Video: VP8 (.webm) - 360p - N/A>],
    def test_select_mp4_over_other_format(self):
        # given
        url = "https://www.youtube.com/watch?v=QegtQLZjVmY"
        # mock Youtube resource
        with open(music_server.config.test_resources_folder + 'test_select_mp4_over_other_format.html') as fh:
            mock_html = fh.read()
        with mock.patch('pytube.api.urlopen') as urlopen:
            urlopen.return_value.read.return_value = mock_html
            yt = api.YouTube()
            yt._js_cache = None
            yt.from_url(url)
        # when
        video = youtube_download.select_video(yt)
        # then
        self.assertEquals(video.extension, 'mp4')
        self.assertEquals(video.filename, u'PRATOS - TANT DE DESIR')
        self.assertEquals(video.resolution, '360p')

    # when multiple mp4 available , assure that we take the highest resolution
    # <Video: MPEG-4 Visual (.3gp) - 144p - Simple>,
    # <Video: MPEG-4 Visual (.3gp) - 240p - Simple>,
    # <Video: H.264 (.mp4) - 360p - Baseline>,
    # <Video: H.264 (.mp4) - 720p - High>,
    # <Video: VP8 (.webm) - 360p - N/A>
    def test_select_video_when_multiple_mp4(self):
        # given
        url = 'https://www.youtube.com/watch?v=yl5WfT7IDDU'
        # mock Youtube resource
        with open(music_server.config.test_resources_folder + 'youtube_multiple_mp4.html') as fh:
            mock_html = fh.read()
        with mock.patch('pytube.api.urlopen') as urlopen:
            urlopen.return_value.read.return_value = mock_html
            yt = api.YouTube()
            yt._js_cache = None
            yt.from_url(url)
        # when
        video = youtube_download.select_video(yt)
        # then
        self.assertEquals(video.extension, 'mp4')
        self.assertEquals(video.filename, u'Roosevelt - Elliot (Official Video)')
        self.assertEquals(video.resolution, '720p')

    # when no mp4 available takes the last results
    # the html resource actually contains mp4 files so it's removed in the youtube object afterward
    # <Video: MPEG-4 Visual (.3gp) - 144p - Simple>,
    # <Video: MPEG-4 Visual (.3gp) - 240p - Simple>,
    # <Video: VP8 (.webm) - 360p - N/A>]
    #todo cant change youtube ovject, change html or find an actual video without mp4 format
#     def test_select_video_when_no_mp4(self):
#         # given
#         url = 'https://www.youtube.com/watch?v=yl5WfT7IDDU'
#         # mock Youtube resource
#         with open(music_server.config.test_resources_folder + 'youtube_no_mp4.html') as fh:
#             mock_html = fh.read()
#         with mock.patch('pytube.api.urlopen') as urlopen:
#             urlopen.return_value.read.return_value = mock_html
#             yt = api.YouTube()
#             yt._js_cache = None
#             yt.from_url(url)
#             browse(yt)
#             # remove the mp4 video
#             videos = []
#             # myvideos = yt.get_videos()
#             videos.append(yt._videos[0])
#             videos.append(yt._videos[1])
#             videos.append(yt._videos[3])
#             yt._videos = videos
#         # when
#         video = youtube_download.select_video(yt)
#         # then
#         self.assertEquals(video.extension, 'webm')
#         self.assertEqual(video.resolution, '360p')

#     def test_youtube_download(self):
#         # todo mock
#         # given
#         url = "https://www.youtube.com/watch?v=io8SgjNcNbk"
#         # when
#         video_path = youtube_download.YoutubeDownload(url).download(music_server.config.tmp_folder)
#         # then
#         self.assertEquals(music_server.config.tmp_folder + 'PRATOS - OSNI.mp4', video_path)

if __name__ == '__main__':
    unittest.main()
