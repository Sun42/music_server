import unittest
from .context import music_server
from music_server import util
from music_server import config

class UtilTestCase(unittest.TestCase):

    def test_remove_extension(self):
        # given
        filename = "video.mp4"
        # when
        trimmed_filename = music_server.util.remove_extension(filename)
        # then
        self.assertEqual(trimmed_filename, "video")

    def test_remove_extension_when_no_extension(self):
        # given
        filename = 'video'
        # when
        trimmed_filename = music_server.util.remove_extension(filename)
        # then
        self.assertEquals(trimmed_filename, 'video')

    def test_remove_extension_when_none(self):
        # given
        filename = None
        # when
        trimmed_filename = music_server.util.remove_extension(filename)
        # then
        self.assertIsNone(trimmed_filename)

    def test_remove_extension_when_empty_name(self):
        # given
        filename = ''
        # when
        trimmed_filename = music_server.util.remove_extension(filename)
        # then
        self.assertEquals(trimmed_filename, '')

    def test_remove_extension_when_multiple_extension(self):
        # given
        filename = 'video.artist.title.mp4'
        # when
        trimmed_filename = music_server.util.remove_extension(filename)
        # then
        self.assertEquals(trimmed_filename, 'video.artist.title')

    def test_remove_extension_when_multiple_dots(self):
        # given
        filename = 'video...mp4'
        # when
        trimmed_filename = music_server.util.remove_extension(filename)
        # then
        self.assertEquals(trimmed_filename, 'video..')
