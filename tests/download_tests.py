import os
import sys
import unittest
from pprint import pprint
from .context import music_server
from music_server import util
from music_server import config
from music_server import download

class DownloadTestCase(unittest.TestCase):

    def setUp(self):
        music_server.util.clean_dir(music_server.config.tmp_folder)

    def tearDown(self):
        music_server.util.clean_dir(config.tmp_folder)

    def test_format_youtube_query(self):
        # given
        search_query = "simple_query"
        expected_result = "http://youtube.com/results?search_query=simple_query"
        # when
        youtube_query = music_server.download.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_format_youtube_query_with_space(self):
        # given
        search_query = "a b"
        expected_result = "http://youtube.com/results?search_query=a+b"
        # when
        youtube_query = music_server.download.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_format_youtube_with_plus(self):
        # given
        search_query = "a+b"
        expected_result = "http://youtube.com/results?search_query=a%2Bb"
        # when
        youtube_query = music_server.download.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_fetch_first_result(self):
        # given
        with open(config.test_folder + 'pratos_osni_html_content', 'r') as myfile:
            html_content = myfile.read()
        expected_result = "io8SgjNcNbk"
        # when
        first_result = music_server.download.fetch_first_result(html_content)
        # then
        self.assertEquals(first_result, expected_result)

    def test_download_video(self):
        #given
        url = "https://www.youtube.com/watch?v=QegtQLZjVmY"
        # when
        video = download.download_video(url)
        # then
        # pprint(vars(video))
        self.assertEquals(video.extension, 'mp4')
        self.assertEquals(video.filename, u'PRATOS - TANT DE DESIR')

    def test_download_video_when_multiple_mp4(self):
        #given
        url = 'https://www.youtube.com/watch?v=yl5WfT7IDDU'
        video = download.download_video(url)
        # then
        # pprint(vars(video))
        self.assertEquals(video.extension, 'mp4')
        self.assertEquals(video.filename, u'Roosevelt - Elliot (Official Video)')
        self.assertEqual(video.resolution, '720p')

    def test_download_video_no_mp4(self):
        pass

    def test_download_first_result(self):
        # given
        search_query = "PRATOS OSNI"
        print ("Test download video with search query: " + search_query)
        # when
        video = download.download_first_result(search_query)
        # then
        print ('Video result: ' + video)
        self.assertFalse(video == "", "Video string is empty")
        self.assertTrue(os.path.isfile(video), "Video is not there")

if __name__ == '__main__':
    unittest.main()
