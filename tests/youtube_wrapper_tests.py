import os
import sys
import unittest
from mock import MagicMock
from mock import patch
from pprint import pprint
from pytube import YouTube

from .context import music_server
from music_server import util
from music_server import config
from music_server import youtube_wrapper

class YoutubeWrapperTestCase(unittest.TestCase):

    def setUp(self):
        music_server.util.clean_dir(music_server.config.tmp_folder)

    def tearDown(self):
        music_server.util.clean_dir(config.tmp_folder)

    def test_format_youtube_query(self):
        # given
        search_query = "simple_query"
        expected_result = "http://youtube.com/results?search_query=simple_query"
        # when
        youtube_query = music_server.youtube_wrapper.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_format_youtube_query_with_space(self):
        # given
        search_query = "a b"
        expected_result = "http://youtube.com/results?search_query=a+b"
        # when
        youtube_query = music_server.youtube_wrapper.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_format_youtube_with_plus(self):
        # given
        search_query = "a+b"
        expected_result = "http://youtube.com/results?search_query=a%2Bb"
        # when
        youtube_query = music_server.youtube_wrapper.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_fetch_first_result_when_empty(self):
        # given
        html_content = None
        # when
        first_result = music_server.youtube_wrapper.fetch_results(html_content, 1)
        # then
        self.assertEquals(first_result, None)

    def test_fetch_first_result_when_no_result(self):
        # given
        html_content = "wrong html content"
        # when
        first_result = music_server.youtube_wrapper.fetch_results(html_content, 1)
        # then
        self.assertEquals(first_result, None)

    def test_fetch_results_limit_one(self):
        # given
        with open(config.test_folder + 'pratos_osni_html_content', 'r') as myfile:
            html_content = myfile.read()
        # when
        results = music_server.youtube_wrapper.fetch_results(html_content, 1)
        # then
        expected_result = "io8SgjNcNbk"
        self.assertEquals(len(results), 1)
        self.assertEquals(results[0], expected_result)

    def test_fetch_results_limit_ten(self):
        # given
        with open(config.test_folder + 'pratos_osni_html_content', 'r') as myfile:
            html_content = myfile.read()
        # when
        results = music_server.youtube_wrapper.fetch_results(html_content, 10)
        # then
        self.assertEquals(len(results), 10)

    def test_fetch_results_no_limit(self):
        # given
        with open(config.test_folder + 'pratos_osni_html_content', 'r') as myfile:
            html_content = myfile.read()
        # when
        results = music_server.youtube_wrapper.fetch_results(html_content)
        # then
        self.assertEquals(len(results), 54)
#
#     def test_download_video(self):
#         #given
#         url = "https://www.youtube.com/watch?v=QegtQLZjVmY"
#         # when
#         video = youtube_wrapper.download_video(url)
#         # then
#         # pprint(vars(video))
#         self.assertEquals(video.extension, 'mp4')
#         self.assertEquals(video.filename, u'PRATOS - TANT DE DESIR')

    # when multiple mp4 available , assure that we take the highest resolution
    def test_select_video_when_multiple_mp4(self):
        #given
        url = 'https://www.youtube.com/watch?v=yl5WfT7IDDU'
        yt = YouTube(url)
        video = youtube_wrapper.select_video(yt)
        # then
        self.assertEquals(video.extension, 'mp4')
        self.assertEquals(video.filename, u'Roosevelt - Elliot (Official Video)')
        self.assertEqual(video.resolution, '720p')
# TODO
#     def test_download_video_no_mp4(self):
#         pass
#     # to mock video.download
#     def test_download_first_result(self):
#         # given
#         search_query = "PRATOS OSNI"
#         # when
#         video = youtube_wrapper.download_first_result(search_query)
#         # then
#         print ('Video result: ' + video)
#         self.assertFalse(video == "", "Video string is empty")
#         self.assertTrue(os.path.isfile(video), "Video is not there")

    def test_download_first_result_when_none(self):
        # given
        search_query = None
        # when
        video = youtube_wrapper.download_first_result(search_query)
        # then
        self.assertEquals(video, None)

    # @patch('music_server.download.fetch_first_result') /*, mock_a*/
    def test_download_first_result_when_fetch_first_result_none(self):
        # mock_a.return_value = MagicMock(response = None)
        # given
        search_query="PRATOS OSNIIII"
        # search_query="PRATOS OSNI"
        # when
        video = youtube_wrapper.download_first_result(search_query)
        # then
        self.assertEquals(video, None)

if __name__ == '__main__':
    unittest.main()
