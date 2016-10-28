import os
import shutil
import tempfile
import unittest
import urllib


from mock import patch
from objbrowser import browse

from .context import music_server
from music_server import music_server
from music_server import config
from music_server import util
from music_server import youtube_download

class MusicServerTestCase(unittest.TestCase):

    def setUp(self):
        music_server.util.clean_dir(music_server.config.tmp_folder)
        self.app = music_server.app.test_client()

    def tearDown(self):
        pass

    def test_root_404(self):
        rv = self.app.get('/')
        assert b'Not found' in rv.data

    #  @todo mock
    def test_search(self):
        # given
        search_query = "pratos osni"
        # when
        rv = self.app.get('/search/pratos osni')
        # then
        assert b'ok' in rv.data

    #todo mock video conversion
    @patch('music_server.youtube_download.YoutubeDownload.download')
    # @patch('music_server.converter.video_to_audio')
    def test_download(self, download_patch):
        # given
        shutil.copy(config.test_resources_folder + "video_ok.mp4", config.tmp_folder + "video_ok.mp4")
        url = urllib.quote('https://www.youtube.com/watch?v=WPw7nlluRdc')
        download_patch.return_value = config.tmp_folder + 'video_ok.mp4'
        # when
        rv = self.app.get("/download/" + url)
        # then
        assert b'http://localhost/music/video_ok.mp3' in rv.data

if __name__ == '__main__':
    unittest.main()
