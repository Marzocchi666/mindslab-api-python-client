#!/usr/bin/env python

from mindslab.client import MindsAPIClient

import unittest
import sys

class TestMindsAPIClient(unittest.TestCase):
    ''' unit test for Minds API client container.
    '''

    client = MindsAPIClient()

    def test_client_initialization(self):
        self.assertFalse(self.client.__eq__(None))
        self.assertTrue(isinstance(self.client, MindsAPIClient))

    def test_client_endpoint(self):
        self.assertTrue(self.client.get_endpoint().__eq__('https://mindsapi.mindslab.ai/api/'))

    def test_client_tag(self):
        self.assertTrue(bool(self.client.get_tag()))

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMindsAPIClient)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(test_suite))
    sys.exit(not result.wasSuccessful())
