#!flask/bin/python

import os
import music_server
import unittest
import tempfile

class MusicServerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = dlmp3.app.test_client()

    def tearDown(self):
        pass
    
    def test_empty_db(self):
        rv = self.app.get('/')
        dir(rv.data)
        assert b'Not found' in rv.data

if __name__ == '__main__':
    unittest.main()
