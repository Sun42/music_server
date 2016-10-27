import unittest
import shutil
from .context import music_server
from music_server import util
from music_server import config
from music_server import converter

class ConverterTestCase(unittest.TestCase):

    def setUp(self):
        music_server.util.clean_dir(music_server.config.tmp_folder)

    def tearDown(self):
        music_server.util.clean_dir(config.tmp_folder)

    def test_video_to_audio__when_mp4(self):
        # given
        video_filename = "video_ok.mp4"
        # copy it to the tmp folder, audio file will be written
        shutil.copy(music_server.config.test_folder + 'video_ok.mp4', music_server.config.tmp_folder)
        video_file = music_server.config.tmp_folder + 'video_ok.mp4'
        # when
        audio_file = music_server.converter.video_to_audio(video_file, music_server.config.tmp_folder)
        # then
        self.assertEquals(audio_file, music_server.config.tmp_folder + 'video_ok.mp3')

if __name__ == '__main__':
    unittest.main()