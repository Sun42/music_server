import os
from .context import music_server
from music_server import music_server
from music_server import config
import unittest
import tempfile

class MusicServerTestCase(unittest.TestCase):

    def setUp(self):
        music_server.util.clean_dir(music_server.config.tmp_folder)
        self.app = music_server.app.test_client()

    def tearDown(self):
        pass

    def test_empty_response(self):
        rv = self.app.get('/')
        dir(rv.data)
        assert b'Not found' in rv.data

    def test_valid_query(self):
        rv = self.app.get('/songs/get/PRATOS/OSNI')
        # dir(rv.data)
        # print(rv.data)
        assert b'pratos-osni.mp3' in rv.data


if __name__ == '__main__':
    unittest.main()
