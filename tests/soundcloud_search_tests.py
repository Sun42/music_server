import unittest
import json

from objbrowser import browse

import music_server
from music_server import config
from music_server import soundcloud_search

class SoundcloudSearchTestCase(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_format_soundcloud_query(self):
            # given
            search_query = "simple_query"
            # when
            query = soundcloud_search.format_query(search_query)
            # then
            expected_result = "https://soundcloud.com/search/sounds?q=simple_query"
            self.assertEqual(query, expected_result)

    def test_fetch_results(self):
        # given
        with open(config.test_resources_folder + 'soundcloud_search_list.html', 'r') as myfile:
            html_content = myfile.read()
        # when
        results = soundcloud_search.fetch_results(html_content)
        # then
        with open(config.test_resources_folder + 'soundclound_search_list.json', 'r') as myfile2:
            expected_links = json.loads(myfile2.read())
        self.assertEqual(results, expected_links)

if __name__ == '__main__':
    unittest.main()