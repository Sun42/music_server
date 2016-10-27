import pdb
import unittest
import json

from objbrowser import browse
import mock
from mock import patch

import music_server
from music_server import youtube_search
from music_server import config

class YoutubeSearchTestCase(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_format_youtube_query(self):
        # given
        search_query = "simple_query"
        expected_result = "http://youtube.com/results?search_query=simple_query"
        # when
        youtube_query = youtube_search.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_format_youtube_query_with_space(self):
        # given
        search_query = "a b"
        expected_result = "http://youtube.com/results?search_query=a+b"
        # when
        youtube_query = youtube_search.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_format_youtube_with_plus(self):
        # given
        search_query = "a+b"
        expected_result = "http://youtube.com/results?search_query=a%2Bb"
        # when
        youtube_query = youtube_search.format_youtube_query(search_query)
        # then
        self.assertEqual(youtube_query, expected_result, "Youtube query formatter failed")

    def test_fetch_first_result_when_empty(self):
        self.assertRaises(TypeError, youtube_search.fetch_results, None)

    # empty list
    def test_fetch_first_result_when_no_result(self):
        # given
        html_content = "wrong html content"
        # when
        result = youtube_search.fetch_results(html_content)
        # then
        self.assertFalse(result, 'Result should be an empty list')

    def test_fetch_results(self):
        # given
        with open(config.test_folder + 'youtube_search_pratos_osni.html', 'r') as myfile:
            html_content = myfile.read()
        with open(config.test_folder + 'youtube_search_pratos_osni.json', 'r') as myfile2:
            expected_links = json.loads(myfile2.read())
        # when
        results = youtube_search.fetch_results(html_content)
        # then
        self.assertEqual(results, expected_links)

    @patch('music_server.youtube_search.get_html')
    def test_youtube_search(self, test_patch):
        # given
        with open(music_server.config.test_folder + 'youtube_search_pratos_osni.html') as fh:
            mock_html = fh.read()
            test_patch.return_value = mock_html
        with open(config.test_folder + 'youtube_search_pratos_osni.json', 'r') as myfile2:
            expected_links = json.loads(myfile2.read())
        # when
            results = youtube_search.YoutubeSearch("pratos osni").video_ids
        # then
        self.assertEqual(results, expected_links)

    def test_search_empty(self):
        # given
        search_query = ''
        # when
        results = youtube_search.YoutubeSearch(search_query)
        # then
        self.assertTrue(results)

    def test_search_none(self):
        # given
        search_query = None
        # when
        results = youtube_search.YoutubeSearch(search_query)
        # then
        self.assertTrue(results)

if __name__ == '__main__':
    unittest.main()