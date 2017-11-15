#!/usr/bin/env python

from mindslab.client import MindsAPIClient
from mindslab.stt import MindsSTTClient

import unittest
import sys

class TestMindsSTTClient(unittest.TestCase):
    ''' unit test for Minds STT client.
    '''

    client = MindsAPIClient()
    stt = MindsSTTClient()

    def test_client_initialization(self):
        self.assertFalse(self.stt.__eq__(None))
        self.assertTrue(isinstance(self.stt, MindsAPIClient))

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMindsSTTClient)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(test_suite))
    sys.exit(not result.wasSuccessful())
