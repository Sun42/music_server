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

    def test_extract_filename(self):
        # given
        file_path = "/home/chris/dir/myfile.txt"
        # when
        filename = music_server.util.extract_filename(file_path)
        # then
        self.assertEquals(filename, 'myfile.txt')


    def test_normalize_to_lower(self):
        # given
        name = 'NoMdeLaRTISTE'
        # when
        normalized_str = util.normalize(name)
        # then
        self.assertEquals(normalized_str, 'nomdelartiste')

    def test_normalize_strip(self):
        # given
        str = '    nomdelartiste     '
        # when
        normalized_str = util.normalize(str)
        # then
        self.assertEquals(normalized_str, 'nomdelartiste')

    def test_normalize_replace_spaces(self):
        # given
        str = 'nom de lartiste'
        # when
        normalized_str = util.normalize(str)
        # then
        self.assertEquals(normalized_str, 'nom_de_lartiste')

    def test_normalize(self):
        # given
        str = ' NoM\tde L\'-artiste- '
        # when
        normalized_str = util.normalize(str)
        # then
        self.assertEquals(normalized_str, 'nom_de_l\'_artiste')

    def test_make_audio_name(self):
        # given
        artist_name = "nOm dE L artiste"
        title = "titre"
        # when
        audio_name = util.make_audio_name(artist_name, title)
        # then
        self.assertEquals(audio_name, 'nom_de_l_artiste-titre.mp3')

    def test_find_in_filesystem_when_present(self):
        # given
        present_file = 'present.mp3'
        # when
        is_present = util.find_in_filesystem(config.test_folder, present_file)
        # then
        self.assertTrue(is_present, "File {} not found".format(present_file))

    def test_find_in_filesystem_when_absent(self):
        # given
        absent_file = 'absent.mp3'
        # when
        is_present = util.find_in_filesystem(config.test_folder, absent_file)
        # then
        self.assertFalse(is_present,  "File {} found".format(absent_file))