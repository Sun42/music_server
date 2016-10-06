import unittest
import shutil
import audiotools
from .context import music_server
from music_server import util
from music_server import config
from music_server import converter

class ConverterTestCase(unittest.TestCase):

    def setUp(self):
        music_server.util.clean_dir(music_server.config.tmp_folder)

    def tearDown(self):
        music_server.util.clean_dir(config.tmp_folder)

    def test_remove_extension(self):
        # given
        filename = "video.mp4"
        # when
        trimmed_filename = music_server.converter.remove_extension(filename)
        # then
        self.assertEqual(trimmed_filename, "video")

    def test_remove_extension_when_no_extension(self):
        # given
        filename = 'video'
        # when
        trimmed_filename = music_server.converter.remove_extension(filename)
        # then
        self.assertEquals(trimmed_filename, 'video')

    def test_remove_extension_when_none(self):
        # given
        filename = None
        # when
        trimmed_filename = music_server.converter.remove_extension(filename)
        # then
        self.assertIsNone(trimmed_filename)

    def test_remove_extension_when_empty_name(self):
        # given
        filename = ''
        # when
        trimmed_filename = music_server.converter.remove_extension(filename)
        # then
        self.assertEquals(trimmed_filename, '')

    def test_remove_extension_when_multiple_extension(self):
        # given
        filename = 'video.artist.title.mp4'
        # when
        trimmed_filename = music_server.converter.remove_extension(filename)
        # then
        self.assertEquals(trimmed_filename, 'video.artist.title')

    def test_remove_extension_when_multiple_dots(self):
        # given
        filename = 'video...mp4'
        # when
        trimmed_filename = music_server.converter.remove_extension(filename)
        # then
        self.assertEquals(trimmed_filename, 'video')

    def test_video_to_audio__when_mp4(self):
        # given
        video_filename = "video_ok.mp4"
        # copy it to the tmp folder, audio file will be written in the same directory and be cleaned after the test
        shutil.copy(music_server.config.test_folder + 'video_ok.mp4', music_server.config.tmp_folder)
        video_file = music_server.config.tmp_folder + 'video_ok.mp4'
        # when
        audio_file = music_server.converter.video_to_audio(video_file)
        # then
        self.assertEquals(audio_file, music_server.config.tmp_folder + 'video_ok.mp3')

if __name__ == '__main__':
    unittest.main()