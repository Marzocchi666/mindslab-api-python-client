#!/usr/bin/env python

from mindslab.client import MindsAPIClient
from mindslab.mrc import MindsMRCClient

import unittest
import sys

class TestMindsMRCClient(unittest.TestCase):
    ''' unit test for Minds MRC client.
    '''

    client = MindsAPIClient()
    mrc = MindsMRCClient()

    def test_client_initialization(self):
        self.assertFalse(self.mrc.__eq__(None))
        self.assertTrue(isinstance(self.mrc, MindsAPIClient))

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMindsMRCClient)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(test_suite))
    sys.exit(not result.wasSuccessful())
